import cv2
from pynput.keyboard import Key, Controller

face_cascade = cv2.CascadeClassifier('haarcascade\\fist.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade\\aGest.xml')
hq = []
vq = []


def instruct(l):
    keyboard = Controller()
    print(l)
    if l[1][0] - l[1][-1] > 80:  # y coordinate increse : hands up
        # Opens Task Manager
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.esc)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.esc)

    if l[1][0] - l[1][-1] < -80:
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.f4)


def cameraWork():
    # capture frames from a camera
    cap = cv2.VideoCapture(0)

    # loop runs if capturing has been initialized.
    while 1:
        # reads frames from a camera
        ret, img = cap.read()
        # convert to gray scale of each frames
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detects faces of different sizes in the input image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            # To draw a rectangle in a face
            hq.append(x)
            if len(hq) == 10:
                hq.pop(0)
            vq.append(y)
            if len(vq) == 10:
                vq.pop(0)
            # print(hq, vq)

            instruct([hq, vq])

            print(x, y, w, h)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
        # Display an image in a window
        cv2.imshow('img', img)
        # Wait for Esc key to stop
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        # Close the window
    cap.release()

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()


def main():
    cameraWork()


if __name__ == '__main__':
    print("While giving instructions, hold fist for 3 seconds")
    main()
