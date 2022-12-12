# OSS_TermProject_Team8   
***
## **About Project:**   
Detecting the face through a webcam, and determines whether the user is taking a class or not.   


After checking the presence or absence of facial recognition by webcam, check and print the attendance of the class.   

If the face is recognized on the webcam, we consider it as taking the class and print its status.    
Else if the face is not recognized on the webcam, we consider it as NOT taking the class and print its status.
***

## **Roles:**   
#### We divided the project into 4 parts/branches:
- Get Numpy array image from webcam  //최민석   
- Preprocessing //이정대   
- Face recognition  //장혁진   
- Determine whether there is a person or not  //임상균 
***

## **Requirements:**
- Install 'mediapipe': ```pip install mediapipe```   
- Haar Cascade XML file for detection:   
https://github.com/opencv/opencv/tree/master/data/haarcascades   
*(XML file name should be same as "haarcascade_frontalface_default" and locates in same dir)*
- python(3.10.6) *(version I test on)*   
- openCV(4.6.0) *(version I test on)*   
- Numpy(1.23.5) *(version I test on)*   
***

## **Command to run the detection:**   
```python
python main.py   
``` 
***

## **Results:**   
After typing ```python main.py```, you can run the detection. It will automatically open the webcam. Every 2 frames(0.5 sec), it will recognize the face and determine whether a person is attending class or not through the presence or absence of face recognition on the webcam. And prints the user's class attendance status every 5 seconds. (To prevent recognition errors, the face is set to be recognized every 2 frames, which may appear to be lagging, but it's NOT) And if it cannot open webcam, it will print a message.

#### See the output results below:   

- #### Face Detected   

![face detected](https://user-images.githubusercontent.com/106862808/207097459-5a49fc74-e734-489d-aaac-439da0c9cd9d.png)   

- #### Face *NOT* Detected   

![face NOT detected](https://user-images.githubusercontent.com/106862808/207097101-9859fde1-7caf-40eb-9772-e14559672e59.png)   

- #### Face Detection changed
![detection changed](https://user-images.githubusercontent.com/106862808/207104920-cd73bdb9-c3a7-4d35-87ec-aece128ecd4d.png)   

- #### Cannot open webcam
![webcam err](https://user-images.githubusercontent.com/106862808/207139829-fc4d8680-f8db-4954-bf3c-51526d4c1590.png)   
***

## **References:**    
#### 
- Using Haar Cascade to detect face through webcam(XML file for detection) :   
https://github.com/opencv/opencv/tree/master/data/haarcascades
- Reffered for webcam configuration :   
https://velog.io/@nayeon_p00/OpenCV-Python-%EC%9B%B9%EC%BA%A0%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-%ED%8A%B8%EB%9E%99%EB%B0%94%EB%A1%9C-%EB%AA%85%EB%8F%84%EC%99%80-%EC%B1%84%EB%8F%84-%EC%A1%B0%EC%A0%95%ED%95%98%EA%B8%B0-%EB%85%B8%EC%9D%B4%EC%A6%88-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0-%EB%9D%BC%EB%B2%A8%EB%A7%81%EC%9C%BC%EB%A1%9C-%EB%AC%BC%EC%B2%B4-%EC%B6%94%EC%A0%81%ED%95%98%EA%B8%B0
- Reffered for preprocessing :
  1. https://greencloud.tistory.com/87
  2. https://www.youtube.com/watch?v=FMaNNXgB_5c
