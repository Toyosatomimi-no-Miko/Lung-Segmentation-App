import streamlit as st
import os
import subprocess

# Define output directory (Change this to your actual output folder)
OUTPUT_DIR = r"D:\Chris\Rabbit data\3D Slicer"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Path to the nnUNet prediction script
SCRIPT_PATH = r"D:\Chris\3D-nnUnet development\rabbit_nnUNet_seg_pipeline\rabbit_nnUNet_seg_pipeline\nnunet_pred_nii.py"

def run_segmentation(input_path):
    """Runs the nnUNet segmentation model on the given input file."""
    command = [
        'python', SCRIPT_PATH, 
        '-i', input_path, 
        '-o', OUTPUT_DIR  # All results go into the same folder
    ]

    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e}")
        return False

def main():
    st.title("nnUNet Segmentation Tool")
    
    # Upload multiple files
    uploaded_files = st.file_uploader(
        "Upload Input Images", 
        type=["nii", "nii.gz", "png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )

    # Store input file paths
    input_paths = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Save file in OUTPUT_DIR to preserve name
            input_path = os.path.join(OUTPUT_DIR, uploaded_file.name)

            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            input_paths.append(input_path)

        # Single button to run segmentation on all files
        if st.button("Run Segmentation on All Files"):
            with st.spinner("Processing images..."):
                for input_path in input_paths:
                    success = run_segmentation(input_path)

                    if success:
                        st.success(f"✅ Segmentation completed for {os.path.basename(input_path)}!")
                    else:
                        st.error(f"❌ Segmentation failed for {os.path.basename(input_path)}. Check logs.")

            st.write(f"📂 All results are saved in: `{OUTPUT_DIR}`")

if __name__ == "__main__":
    main()
