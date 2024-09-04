import cv2
import numpy as np
from ultralytics import YOLO

def crop_image(image, top, left, right):
    polygon = np.array([[0, image.shape[0]], [left[0], left[1]], [top[0], top[1]], [right[0], right[1]], [image.shape[1], image.shape[0]]], np.int32)
    polygon = polygon.reshape((-1, 1, 2))

    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [polygon], 255)

    masked_image = cv2.bitwise_and(image, image, mask=mask)

    x, y, w, h = cv2.boundingRect(polygon)
    cropped_image = masked_image[y:y+h, x:x+w]

    return cropped_image

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Use a smaller model for faster processing

# Initialize video capture
cap = cv2.VideoCapture('Videos\\01.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (int(cap.get(3) // 2), int(cap.get(4) // 2)))  # Reduce resolution by half

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break


    # Reduce frame size for faster processing
    frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

    # Reset vehicle count for the current frame
    vehicle_count = 0

    # Perform object detection
    results = model(frame)

    # Count vehicles
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)  # Convert tensor to integer
            label = result.names[cls_id]
            if label in ['car', 'truck', 'bus', 'motorbike']:
                vehicle_count += 1


    top = (538 // 2, 891 // 2)
    right = (1079 // 2, 1491 // 2)
    left = (0, 1727 // 2)

    frame = crop_image(frame, top, left, right)
    frame = cv2.resize(frame, (500, 700))

    # Display vehicle count
    cv2.putText(frame, f'Vehicle Count: {vehicle_count}', (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Write the frame into the file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
