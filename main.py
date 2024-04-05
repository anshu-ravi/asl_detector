import cv2
import argparse

from ultralytics import YOLO
import supervision as sv
import numpy as np

from audio import speak

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ASL Alphabet Detector")
    parser.add_argument(
        "--webcam-resolution", 
        default=[460, 460], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args

def asl_detector(frame: np.ndarray, model: YOLO) -> np.ndarray:
    result = model(frame)[0] 
    detections = sv.Detections.from_ultralytics(result)

    # Create an instance of BoundingBoxAnnotator
    annotator = sv.BoundingBoxAnnotator()
    annotated_image = annotator.annotate(frame, detections)

    if not isinstance(annotated_image, np.ndarray):
        annotated_image = np.array(annotated_image)

    all_labels = []
    # Loop through detections to add labels
    for i in range(len(detections)):
        label = detections.data['class_name'][i]
        cf = detections.confidence[i]
        label_text = f"{label}: {cf:.2f}"
        all_labels.append(label)

        bbox = detections.xyxy[i]
        x1, y1, x2, y2 = bbox

        # Explicitly convert coordinates to integers
        x1, y1 = int(x1), int(y1)

        # Use OpenCV to put text on the image
        # Ensure coordinates and font scale are correctly typed
        cv2.putText(annotated_image, label_text, 
                    (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, (255, 255, 255), 2)

    return annotated_image, all_labels

def main(model: YOLO):
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    try: 
        while True:
            ret, frame = cap.read()

            frame = cv2.flip(frame, 1)

            annotated_image, labels = asl_detector(frame, model)
            
            cv2.imshow("ASL Detector", annotated_image)

            if labels:
                speak(" ".join(labels), "asl")

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
    


if __name__ == "__main__":
    model = YOLO("best.pt")

    main(model)