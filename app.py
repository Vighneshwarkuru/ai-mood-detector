import cv2
import mediapipe as mp
from deepface import DeepFace

# 🎥 Initialize Camera
cap = cv2.VideoCapture(0)

# 🧑 Face Detection Setup
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()

def analyze_emotion(face_roi):
    """Detect dominant emotion from a cropped face image."""
    try:
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return "neutral"

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera feed failed!")
        break

    frame = cv2.flip(frame, 1)  # Flip for natural mirroring
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            h, w, c = frame.shape
            x, y, width, height = (int(bboxC.xmin * w), int(bboxC.ymin * h),
                                   int(bboxC.width * w), int(bboxC.height * h))
            
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
            face_roi = frame[y:y+height, x:x+width]

            if face_roi.shape[0] > 10 and face_roi.shape[1] > 10:
                mood = analyze_emotion(face_roi)
                cv2.putText(frame, f"Mood: {mood}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                print(f"😊 Detected Mood: {mood}")

    cv2.imshow("Mood Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
