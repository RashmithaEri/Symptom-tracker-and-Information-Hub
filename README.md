# Symptom-tracker-and-Information-Hub
**TITLE:**
"SYMPTOM TRACKER AND INFORMATION HUB"

**AIM:** 
Many people encounter health problems or symptoms and turn to the internet for answers before seeing a doctor. However, the abundance of online medical information can be confusing and not always trustworthy. By creating a symptom tracker, users gain access to a reliable and easy-to-use tool. They can input their symptoms and receive accurate information about potential conditions or what steps to take next, providing peace of mind and guidance when navigating health concerns.

**PYTHON PACKAGES:**
- Pandas: Utilized for data manipulation and analysis.
- Regular Expressions (re module): Employed for text processing and pattern matching.
- Tkinter: Utilized for creating the graphical user interface (GUI).
- Matplotlib: Utilized for generating visualizations such as bar plots, aiding in the representation of data.

**DATA FLOW:**
Users will input their symptoms through a user-friendly interface, which can be either a command-line interface or a graphical user interface (GUI) developed using libraries like Tkinter. The application employs regular expressions to process these symptoms, identifying relevant keywords and patterns. Subsequently, it utilizes Matplotlib to generate visualizations such as bar plots representing the frequency of various symptoms or conditions. After the user submits their symptoms, it displays a message box with the matched conditions and generates a bar plot depicting the frequency of each condition. The data flow begins with user input, which triggers symptom matching and visualization processes, and concludes with the presentation of matched conditions and their frequencies. This interactive system efficiently assists users in identifying potential health issues based on reported symptoms, enhancing medical decision-making.

**INPUT/OUTPUT:**
- Input: Users enter symptoms separated by commas in the GUI entry field and click "Submit."
- Output: A message box shows the input symptoms and matching medical conditions. Additionally, a bar plot displays the frequency of each matched condition.
