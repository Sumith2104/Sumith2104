Required Packages and Libraries to Run the Project

To successfully compile and run this Java-based Barcode Attendance System, make sure the following libraries are downloaded and properly added to your project build path:

1. OpenCV Library
   - JAR File: opencv-4xx.jar
   - DLL File: opencv_java4xx.dll
   - Used for: Face detection (if integrated later), image processing.
   - Add the JAR to your build path and place the DLL in your system path (or specify it in code).

2. ZXing (Zebra Crossing)
   - JAR File: core-3.5.2.jar
   - JAR File: javase-3.5.2.jar
   - Used for: Reading and decoding barcodes (QR/linear).

3. Apache POI
   - JAR Files Needed:
     - poi-5.2.3.jar
     - poi-ooxml-5.2.3.jar
     - poi-ooxml-schemas-5.2.3.jar
     - xmlbeans-5.2.3.jar
     - commons-collections4-4.4.jar
     - commons-compress-1.21.jar
     - curvesapi-1.06.jar
   - Used for: Reading from and writing to Excel files for storing attendance data.

4. Java Development Kit (JDK)
   - Recommended Version: Java 8 or higher
   - Make sure JAVA_HOME is set and JDK is installed correctly.

Note: Ensure all JAR files are added to the classpath in your IDE (like Eclipse/IntelliJ) or included while compiling through command line.






