# Lung-Segmentation-App

Open two terminals (Windows Powershell)

In the first terminal, run:

D:

cd Chris\3D-nnUnet development\rabbit_nnUNet_seg_pipeline\rabbit_nnUNet_seg_pipeline

streamlit run app.py

Then the tab http://localhost:8501 will be automatically open on your browser, after uploading all iamge files, wait for a few seconds and click the Run button.

After running, you can check messages (successful or not) in the tab, also ensure that results are in the result folder.

Then in the second terminal, run:

taskkill /f /im streamlit.exe

Then close the tab.
