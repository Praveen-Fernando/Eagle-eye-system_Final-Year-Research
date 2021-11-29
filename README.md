# Eagle-eye-system_Final-Year-Research

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/logo.png?raw=true" alt="logo" width="200"><br>
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/EAGLEEYE%20SYSTEM%402x.png?raw=true" alt="logo" width="200">
 </p>

<p align="justify"> 
It is with great pleasure I would like to mention that our team successfully completed the 4th year research project of SLIIT on criminal investigation and management utilizing CCTV footages named “Eagle Eye”. We believe that this system will immensely help the law enforcement authorities of our country to detect the criminal involved in a crime accurately and in a shorter time duration and help to ensure the law and justice to the victims, their families and to the society as well.
</p>

<p align="justify">  
This system includes features such as Image Enhancement, Abnormal Behavior Detection, Face Detection and Recognition, Figure Recognition and this system is capable of analyzing the whole incident recorded in the CCTV footage/s and identifying the criminal’s face and the weapons used by the criminal accurately. These provide strong scientific evidence for the law enforcement authorities to bring them to the justice. Further, we believe that this system will help the authorities to clear the investigation cases not yet completed due to difficulties they undergo in detecting the real criminal from available CCTV footages.
</p>


**Main objective**

<p align="justify"> 
This research study is designed to detect and identify criminals in less time with high accuracy, better than the existing methods, using their faces, figures, and behaviors followed by the image enhancement process.
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/Capture-copy.jpg" alt="logo" width="70%">
 </p>

**Main Research questions**

<p align="justify"> 
Most of the time, the quality of the CCTV footage are low. Increasing the quality of the footage is important and Authorities don't know the exact time when the suspicious activities happen in CCTV footage. So, the concentration of authorities on each case simultaneously decreases gradually with time. Using manual methods for identifying the criminals' faces are time-consuming and costs higher labor and It can Misidentify persons who have identical faces/features and difficult to identify human age and gender with high variability in a movement such as walking, running, etc. To minimize the disadvantages explained above, a computerized identification system can be utilized. Currently, there is no such system in police and at CID of Sri Lanka.
</p>


**Use of System**

To run the main scan of the system, first users need to upload the CCTV footage into the system.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/upload.JPG?raw=true" alt="logo" width="70%">
 </p>


**Individual Objectives**


**Component 1 - Image Enhancement  | Dewmal Fernando**
<p align="justify"> 
The enhancement feature will be the first step of the system. We use images to capture suspected persons by using CCTV footage. Those images may not be fit for the upcoming processes to handle. It is necessary to have a good quality image to get an accurate result when the system detects faces, figures, and behaviors. We are hoping to increase the processing speed and increase the quality of the captured images by using our image enhancement method than other existing methods available in the industry.
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/1.JPG?raw=true" alt="logo" width="70%">
 </p>

<p align="justify"> 
Mainly, video footage is taken by the system as the input. When this process runs, the video footage is broken into frames. Then the frames will be going through a contrast enhancement process. After this process is done, the frames will be going through an image sharpening mechanism in order to enhance the sharpness of the images. After that, the frames will be going through a noise identification process using a convolutional neural network (CNN) model. From this process, the system will identify the noise type of each frame and apply the suitable denoising method. Then again, the frames will be gone through another process which is a smoothing process. After this process is done, the enhanced frames will be converted to video footage and saved in the database. This system can identify the most common noise types such as Gaussian noise, Salt noise, Pepper noise, and salt and pepper noise. The CNN model is trained using more than 2750 positive and negative images. For the smoothing process, the bilateral filter is used.
</p>

As a additional feature users are able to run the image enhancement process separately as their need.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/image.JPG?raw=true" alt="logo" width="70%">
 </p>


**Component 2 - Abnormal Behavior Detection | Givindu Perera**

<p align="justify"> 
Abnormal Behavior Detection with threatening weapons feature as our second step of the system, We concentrated on two specific tasks: automatic detection and identification of dangerous behaviors in public and restricted locations. Our proposed algorithms can identify suspicious behavior accompanied by threatening weapons that persons are carrying, such as guns or knives (the most often used weapons in attacks) held in a person's hand.
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/2.JPG?raw=true" alt="logo" width="70%">
 </p>
 
<p align="justify"> 
In order to detect abnormal behaviors in CCTV footage, 3 sub-objectives were mainly used, 1. Detection of all the humans in CCTV footage that appears. 2. Detection of suspects with threatening weapons in the detected frames that contain all the humans (including normal people). 3. Classify the details of the detected abnormal activity and type of the detected weapon on CCTV footage.
</p>

<p align="justify"> 
To implement these objectives, the system was developed with 3 main stages. These are the Human detection stage, the Behavior analyzing stage, and the Finalizing stage. The first stage takes the enhanced CCTV footage as input, breaks it down into frames, and extracts the features. Then, in all the frames, look for Humans and store them in a system folder. The behavior analysis stage will next build a video using the human identified frames as input. The system will then use this video to recognize frames that contain behaviors with threatening weapons and classify them using the data model to determine whether it was a shooting or stabbing attack. The frames that were recognized as suspicious, as well as the kind of occurrence, will be saved in a CSV file and a particular table in the MySQL system database for use by the next procedures. Deep Neural network methods were utilized to build this system; for human detection, the MobileNet SSD algorithm was used, and for weapon detection, the YOLO version 4 algorithm was used. The 12,000-picture dataset was utilized to train the custom YOLO version 4 model, and the training procedure was carried out using Google co-laboratory. In addition, Image processing, deep learning, python, OpenCV, and Electron JS were utilized as technologies, and Caffe and YOLO Darknet were used as frameworks.
</p>

As a additional feature users are able to run abnormal behavior detection process separately as their need.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/behavior.JPG?raw=true" alt="logo" width="70%">
 </p>


**Component 3 - Criminal’s Face Detection and Recognition | Praveen Fernando**

<p align="justify"> 
Criminal’s Face Detection and Recognition feature as our third step of the system, we focused and target to capture the suspect’s face efficiently from CCTV footage and compare it with the system’s database that contains a registered Criminals faces using image processing and facial landmarking algorithms, which helps to capture suspect’s face and matching the Criminals faces with the facial measurements of the detected face in the database.
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/3.JPG?raw=true" alt="logo" width="70%">
 </p>
 
<p align="justify"> 
In Face detection and recognition, the component gets the snapshots of the abnormally behaved people with the weapons. Then the system converted them to a video to maximize the speed of the system. The created video passes to the “face detection stage.” In this stage, the input Video will be feature extracted and it moves to the next process to resize the video to support detection of the human face from video. In the face detection step, the suspect's face will detect and store the face temporarily for the next stage. These detected faces will move to the ‘measuring stage.’ In this stage, the input video will be passing through two stages, they are “facial features analysis” and “facial landmark points analysis/measure face according to the different head pose variations.” After passing these two-stage, systems will store these identified suspects' faces temporarily for the final stage of “Identification.” In the ‘identification stage,’ the system compares the faces by analyzing the Stored Criminals' faces one by one with the help of the system database, criminals that are already registered in the system. Finally, the system recognizes the criminal’s face and stores the recognized criminal’s details for the final evaluation. Trained a custom Haar-cascade model to develop the face detection process with help of “Cascade Trainer GUI” software. To improve the accuracy level, developers used nearly 15000 positive and negative images to train this model. In addition, Caffe model, facial landmarking algorithms, LBPH, Haar-cascade algorithm, and CNN algorithms and technologies such as python, OpenCV, Electron js, Image processing, Machine learning were used to develop this Face detection and recognition component.
</p>

As a additional feature users are able to run Face Detection and Recognition process separately as their need.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/face.JPG?raw=true" alt="logo" width="70%">
 </p>
 
 
**Component 4 - Suspect identification with Figure Recognition | Kasun Gunatilleke**

<p align="justify"> 
Suspect identification with Figure Recognition feature as our final step of the system, our target is to capture the suspect person’s figure from the CCTV footage and recognize the person’s body measurements such as body Height, Gender, Age and compares those details with the system database and identify the suspect with matching characteristics using machine learning and image processing algorithms.
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/4.JPG?raw=true" alt="logo" width="70%">
 </p>

<p align="justify"> 
In the Figure recognition component, there are 3 stages. They are the recognition stage, measuring stage, and identification stage. Before the first stage system convert, abnormal behavior detected frames to a video. The system identifies the age and gender of the suspect in the first stage and saves recognized details to the system database. To recognize the age and the gender of the suspect I trained a custom yolo version 4 model with 14142 labeled images using Google Collaboratory. After that, in the measuring stage, the system measures the figure details of the suspect and saves the identified details to the system database. For this height recognition, the dataset contains nearly 5000 people. Finally in the identifying stage system compare identified details with the registered criminal records and identify the criminal and store identified details for the final output. In addition to that Yolo, the darknet is used as the framework. python, image processing, deep learning, and OpenCV are used as the technologies.
</p>

As a additional feature users are able to run the Figure Recognition process separately as their need.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/figure.JPG?raw=true" alt="logo" width="70%">
 </p>


**Technologies and Algorithms**

- [x] YOLO version 4 Algorithm
- [x] Mobile-net-SSD Algorithm
- [x] Deep Neural Network (DNN)
- [x] Haar-Cascade Algorithm
- [x] Local Binary Pattern Histogram (LBPH) 
- [x] Convolutional Neural Network (CNN)
- [x] Python
- [x] Electron JS
- [x] Image Processing
- [x] Deep learning 
- [x] Machine learning
- [x] Open CV
- [x] Dlib
- [x] NCIS
- [x] Caffe Framework
- [x] YOLO Darknet Framework


**Testings and Results**

<p align="justify"> 
For testing purposes, we used 44 CCTV footages relevant to the different categories of crimes. From the footage, 10 robbery cases, 5 aggravated assault cases, 4 weapons dealing, 3 CCTV footages motor vehicle theft cases, 2 kidnapping cases, 8 murder cases, and 12 fighting in public cases. Out of all these CCTV footages, the “Eagle Eye” system could identify over 92% of the criminal cases, compared to the existing systems mentioned in the literature review.
</p>

<p align="justify"> 
As a final result, the system displays the details of the detected criminal’s such as Name, Date of birth, Nic, address, blood group, and criminal’s figure details such as height, age, gender and detected abnormal behavior and the types of the weapons that used, according to the inserted CCTV footage. 
</p>

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/success.JPG?raw=true" alt="logo" width="70%">
 </p>
 
 <p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/Picture2.jpg?raw=true" alt="logo" width="70%">
 </p>


Finally, I would like to thank all my team members who worked hard with dedication for nearly one year as a team to make this project a success.

<p align="center">
    <img src="https://github.com/Jaypraveen/Eagle-eye-system_Final-Year-Research/blob/main/UI/Readme_Imgs/Picture7.png?raw=true" alt="logo" width="70%">
 </p>


**Visit Now** : https://eagleeyesystem.azurewebsites.net/ 
