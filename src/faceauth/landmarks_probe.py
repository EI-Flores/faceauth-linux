from pathlib import Path

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "face_landmarker.task"


def main() -> int:
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found: {MODEL_PATH}")
        print("Download it into models/face_landmarker.task")
        return 1

    camera_index = 0
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"ERROR: Could not open camera index {camera_index}")
        return 1

    base_options = python.BaseOptions(model_asset_path=str(MODEL_PATH))

    options = vision.FaceLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_faces=1,
        output_face_blendshapes=True,
        output_facial_transformation_matrixes=True,
        min_face_detection_confidence=0.5,
        min_face_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    frames_checked = 0
    faces_detected = 0

    try:
        with vision.FaceLandmarker.create_from_options(options) as landmarker:
            while frames_checked < 150:
                ok, frame = cap.read()

                if not ok or frame is None:
                    print("ERROR: Could not read frame from camera")
                    return 1

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=rgb_frame,
                )

                timestamp_ms = frames_checked * 33
                result = landmarker.detect_for_video(mp_image, timestamp_ms)

                frames_checked += 1

                if result.face_landmarks:
                    faces_detected += 1
                    landmarks = result.face_landmarks[0]

                    blendshape_count = 0
                    if result.face_blendshapes:
                        blendshape_count = len(result.face_blendshapes[0])

                    print(
                        "Face detected | "
                        f"landmarks={len(landmarks)} | "
                        f"blendshapes={blendshape_count} | "
                        f"frame={frames_checked}"
                    )

                elif frames_checked % 30 == 0:
                    print(f"No face detected yet | frame={frames_checked}")

    finally:
        cap.release()

    if faces_detected == 0:
        print("RESULT: FAIL - no face detected")
        return 1

    print(f"RESULT: OK - face detected in {faces_detected}/{frames_checked} frames")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())