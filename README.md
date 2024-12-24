### README.md

```markdown
# Wikipedia API Desktop Application

This project is a simple desktop application that utilizes the **Wikipedia API** to search and retrieve summary information about topics. The application is built using Python's `tkinter` module for the graphical user interface (GUI) and the `wikipedia` Python library for fetching data from Wikipedia.

---

## Features

- **Search Wikipedia:** Users can enter a topic and fetch its summary from Wikipedia in Turkish.
- **Clear Input and Output:** A "Clear" button is provided to reset both the input field and the display area.
- **Scrollable Output:** The results are displayed in a text box with horizontal and vertical scrollbars for easy navigation.
- **Error Handling:** If there is an issue with the search (e.g., the topic doesn't exist), a descriptive error message is displayed.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**
- The `wikipedia` Python library. Install it using:
  ```bash
  pip install wikipedia
  ```

---

## How to Run the Application

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the `main.py` file:
   ```bash
   python main.py
   ```

---

## Usage

1. Enter a topic in the input field.
2. Click the **Search** button to fetch the Wikipedia summary.
3. The summary will appear in the text box below.
4. Use the **Clear** button to reset the input and output fields.

---

## File Structure

- `main.py`: The main script that contains the application logic.

---

## Code Overview

### GUI Components

- **Input Field:** Used for entering the search query.
- **Buttons:** 
  - **Search Button** triggers the `search` function to fetch data from Wikipedia.
  - **Clear Button** calls the `clear` function to reset the fields.
- **Text Box:** Displays the fetched Wikipedia summary with scrollbars for navigation.

### Functions

1. `clear()`: Clears the input field and text box.
2. `search()`: Fetches the Wikipedia summary for the entered query and displays it in the text box. If an error occurs, an appropriate message is displayed.

---

## Potential Improvements

- Add support for multiple languages using a dropdown menu.
- Display more detailed information, such as page links or references.
- Include an option to save the search result to a text file.
- Enhance the error handling for network-related issues.

---

## License

This project is open-source and available under the MIT License.

---

## Credits

- **Python Libraries:**
  - `tkinter`: For building the GUI.
  - `wikipedia`: For fetching data from the Wikipedia API.
```
