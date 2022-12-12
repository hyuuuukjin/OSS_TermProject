# OSS_TermProject_Team8   
***
## **About Project:**   
Detecting the face through a webcam, and determines whether the user is taking a class or not.   


After checking the presence or absence of facial recognition by webcam, check and print the attendance of the class.   
If the face is recognized on the webcam, we consider it as taking the class and print its status.    
Else if the face is not recognized on the webcam, we consider it as NOT taking the class and print its status.
***

## **Roles:**   
#### We divided into 4 parts:
1. Get numpy array image from webcam  //최민석   
2. Preprocessing //이정대   
3. Face recognition  //장혁진   
4. Determine whether there is a person or not  //임상균 
***

## **Before start**
*You have to install 'mediapipe' by command: ```pip install mediapipe```*   
***

## **Command to run the detection:**   
```python
python main.py   
``` 
***

## **Result:**   
After typing ```python main.py```, you can run the detection. It will automatically open the webcam. Every 2 frames(0.5 sec), it will recognize the face and determine whether a person is attending class or not through the presence or absence of face recognition on the webcam. And prints the user's class attendance status every 5 seconds. (It is set to recognize face every 2 frames, so it may seem like lagging, but it's NOT)

#### See the output results below:   

- #### Face Detected   

![face detected](https://user-images.githubusercontent.com/106862808/207097459-5a49fc74-e734-489d-aaac-439da0c9cd9d.png)   

- #### Face *NOT* Detected   

![face NOT detected](https://user-images.githubusercontent.com/106862808/207097101-9859fde1-7caf-40eb-9772-e14559672e59.png)   

- #### Face Detection changed
![detection changed](https://user-images.githubusercontent.com/106862808/207104920-cd73bdb9-c3a7-4d35-87ec-aece128ecd4d.png)   
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
