import cv2
import mediapipe as mp
import pyautogui

# ক্যামেরা এবং মিডিয়াপাইপ সেটআপ
cam = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1) # স্ক্রিন রিভার্স করার জন্য
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        # এখানে ৪৭৪ থেকে ৪৭৮ ল্যান্ডমার্কগুলো চোখের মণির জন্য
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            
            # মাউস মুভমেন্ট লজিক (শুধুমাত্র একটি পয়েন্টের জন্য)
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

    cv2.imshow('Eye Mouse Control', frame)
    
    # 'q' চাপলে প্রোগ্রাম বন্ধ হবে
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()