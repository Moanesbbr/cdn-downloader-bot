# CDN Downloader Bot

The **CDN Downloader Bot** is a Python-based tool designed to simplify the process of downloading CSS and JavaScript assets from CDN links and generating their corresponding local `<link>` and `<script>` declarations. With its user-friendly GUI, you can easily configure folder paths, input CDN links, and manage assets for your projects.

## Features

- Automatically downloads CSS and JavaScript files to local folders.
- Generates local declarations for use in projects (e.g., Laravel's `asset()` helper).
- Skips downloading files that already exist.
- User-friendly GUI with input fields, processing buttons, and output display.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cdn-downloader-bot.git
   cd cdn-downloader-bot
   ```

2. Install required dependencies:

   ```bash
   pip install requests
   ```

3. Run the tool:
   ```bash
   python cdns.py
   ```

## Usage

1. Launch the application using `python cdns.py`.
2. Configure folder paths for JavaScript and CSS assets if necessary.
3. Paste CDN links (e.g., `<link>` and `<script>` tags) into the input box.
4. Click **Process CDNs** to download files and generate local declarations.
5. Copy the output declarations and use them in your project.

## Example

### Input

```html
<link href="https://example.com/styles.css" rel="stylesheet" />
<script src="https://example.com/script.js"></script>
```

### Output

```html
CSS Declarations:
<link rel="stylesheet" href="{{ asset('css/plugins/styles.css') }}" />

JavaScript Declarations:
<script src="{{ asset('js/plugins/script.js') }}"></script>
```

## Requirements

- Python 3.6+
- Libraries: `requests`, `tkinter` (built-in)

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
