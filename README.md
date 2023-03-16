# yolov5-aim-assist
An augmented aim assist made for Krunker.IO with the YOLOv5 Object Detection Model.

<h1>Installation</h1>
<ul>
  <li>Install Docker</li>
  <li>Install Windows Subsystem For Linux</li>
  <li>Git clone or download the zip on this project</li>
</ul>

<h1>How to Use</h1>
Keep in mind this is more of an assistant than a bot. You still would carry on playing as you normally would but this time you have a helping hand to play the game with you that locks onto enemies and shoots them. A bit like self-driving cars.
<ul>
  <li>Open powershell</li>
  <li>Type wsl and hit enter</li>
Type these three docker commands:
  <ul>
    <li>cd: cd into the project directory</li>
    <li>sudo dockerd</li>
    <li>In a new wsl tab, run sudo docker run --net=host roboflow/inference-server:cpu</li>
  </ul>
  <li>Now, in the code editor of your choice, <strong>whilst still keeping the terminal window open in the background,</strong> run the main.py script</li>
  <li>You should see an output in the terminal saying 'Not Detected'</li>
  <li>Now open Krunker whilst still keeping the script running in the background</li>
  <li>The script automatically locks onto enemies and (tries to) shoot(s) them</li>
</ul>

<h1>Exiting the Script</h1>
Just go to your code editor and press the stop executing button on the script. Remember to close the wsl windows as well.
