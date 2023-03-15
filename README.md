# yolov5-aim-assist
An augmented aim assist made for Krunker.IO with the YOLOv5 Object Detection Model.

<h1>Installation</h1>
<ul>
<li>Run <code>pip install -r requirements.txt</code> in your desired work environment; I use VS Code.</li>
<li>Open the Google Colab Notebook.</li>
<li>Replace the roboflow code with your own if you wish. When you navigate to your roboflow dataset, you can click export and then copy the 'YOLOv5 and PyTorch' download code to that code cell.</li>
<li>Run all of the commands and set the train command to <code>!python train.py --img 416 --batch 16 --epochs 500 --data {dataset.location}/data.yaml --weights yolov5s.pt --cache</code>.</li>
<li>You can test your trained model with <code>!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source {dataset.location}/test/images</code>; this is explained in the notebook.</li>
<li>Once training of the model is complete, in the Google Colab file directory, navigate to <code>yolov5/runs/train/exp/weights</code> and copy the <code>best.pt</code> weights file into a new VS Code project, or you could use the weights file attached to this repository.</li>
<li>Download the <code>main.py</code> file into the same project and directory as the <code>best.pt</code> file.</li>
</ul>

<h1>How to Use</h1>
Keep in mind this is more of an assistant than a bot. You still would carry on playing as you normally would but this time you have a helping hand to play the game with you that locks onto enemies and shoots them. A bit like self-driving cars.
<ul>
<li>Now, just run the <code>main.py</code> script!</li>
<li>Select Krunker (hopefully more games being supported soon!).</li>
<li>Wait a few seconds and then a window should pop up with what the AI sees. You can minimise it if you wish.</li>
<li>Play the game!</li>
</ul>
