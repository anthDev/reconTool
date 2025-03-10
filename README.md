# reconTool
A USB-based tool to detect connected iPhones, collect device information, and attempt controlled memory writes to analyze security behavior. Includes logging and debugging features for research purposes.


# Features of the Project
	1.	Device Detection
	•	Detect when an iPhone is connected via USB.
	•	Identify the model, iOS version, and SecureROM version (if possible).
	2.	Data Collection
	•	Retrieve basic device descriptors (e.g., Vendor ID, Product ID, Serial Number).
	•	Attempt to access control endpoints (EP0_IN and EP0_OUT).
	•	Log USB transactions and responses.
	3.	Memory Testing (Ethical & Controlled)
	•	Attempt to write data to restricted memory areas to test SecureROM protections.
	•	Capture system responses and potential crashes (without harming the device).
	4.	Logging & Debugging
	•	Collect detailed logs of all USB communications.
	•	Detect unusual behavior in the USB stack, like unexpected resets or stalls.
# Tech stack
	•	Python (pyusb for USB communication)
	•	C (for lower-level USB interactions if needed)
	•	libusb (cross-platform USB library)
	•	Linux/macOS (Preferred OS for running the tool)
