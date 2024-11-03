 图片转 Excel 报价工具

朱元昊 made with GPT Canvas

该工具旨在使用OCR从图片中提取数据，并将处理后的信息导出为 Excel 文件。以下是设置和运行该工具的说明。

前提条件

使用该工具之前，请确保已安装以下内容：

1. Python：版本 3.6 或更高。

2. 所需的 Python 库：
   - pandas：用于处理数据框和导出到 Excel。
   - pytesseract：用于从图片中提取文本的 OCR。
   - Pillow：用于图像处理。
   - openpyxl：用于写入 Excel 文件。
   你可以使用以下命令安装这些库：
       pip install pandas pytesseract Pillow openpyxl

3. Tesseract OCR：安装 Tesseract OCR 软件并将其添加到系统的 PATH 中。你可以从 GitHub 下载。

包含的文件

- quotation.py：执行 OCR 处理图片并将提取的数据导出为 Excel 文件的 Python 脚本。
- 报价.bat：一个批处理文件，允许你通过双击运行 Python 脚本。

使用方法

1. 准备图片文件：将所有需要处理的图片文件（.png、.jpg、.jpeg、.tiff、.bmp、.gif）放置在与 Python 脚本相同的目录中。

2. 运行工具：
   - 双击 报价.bat 文件。这将执行 Python 脚本，处理目录中的所有图片文件，并生成相应的 Excel 文件。

3. 输出：
   - 每个图片文件都会生成一个同名的 Excel 文件，包含提取的数据。

注意事项

- Python 脚本假设图片中包含结构化的行数据，每行包括数量、单价和总价。
- 脚本从图片中提取数值数据，并计算其他列，如以美元表示的单价和总价。
- 如果在图片中未找到有效数据，将显示错误消息。

疑难解答

- 找不到 Tesseract：确保已安装 Tesseract OCR 并将其添加到系统的 PATH 中。你可以通过在命令提示符中运行 tesseract --version 来验证安装。
- 缺少库：如果遇到导入错误，请确保已安装所有必需的 Python 库。
