import cv2


def main() -> int:
    camera_index = 0

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"ERROR: Could not open camera index {camera_index}")
        return 1

    ok, frame = cap.read()
    cap.release()

    if not ok or frame is None:
        print("ERROR: Camera opened but frame capture failed")
        return 1

    height, width = frame.shape[:2]

    print("Camera opened successfully")
    print(f"Resolution: {width}x{height}")
    print("Frame captured: OK")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())