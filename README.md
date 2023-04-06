# OCR Code
This Python script uses Tesseract OCR to recognize text in images and then extracts any occurrence of an eight-character string containing uppercase letters and digits.
## Installation
1. Clone or download the script.
2. Create a virtual environment by running the following command in the terminal:<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash p-4">python3 -m venv venv
`</code></div></div></pre>
3. <code class="!whitespace-pre hljs language-bash p-4">Activate the virtual environment with the following command:<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash p-4"><span class="hljs-built_in">source</span> venv/bin/activate
`</code></div></div></pre></code>
4. <code class="!whitespace-pre hljs language-bash p-4"><code class="!whitespace-pre hljs language-bash p-4">Install the required packages with pip:<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash p-4">pip install -r requirements.txt
`</code></div></div></pre></code></code>
5. <code class="!whitespace-pre hljs language-bash p-4"><code class="!whitespace-pre hljs language-bash p-4"><code class="!whitespace-pre hljs language-bash p-4">To run the script, use the following command:<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash p-4">python main.py
`</code></div></div></pre><code class="!whitespace-pre hljs language-bash p-4">This will process all the images in the "images/new" directory, recognize the text in each image, and extract any eight-character strings containing uppercase letters and digits. The processed images will be moved to the "images/decoded" directory.</code></code></code></code>
6. <code class="!whitespace-pre hljs language-bash p-4"><code class="!whitespace-pre hljs language-bash p-4"><code class="!whitespace-pre hljs language-bash p-4">To exit the virtual environment, run the following command:<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash p-4">deactivate
`</code></div></div></pre></code></code></code>


Note: The output directory will be created automatically if it does not exist.
### Ubuntu
To install Tesseract and its developer tools on Ubuntu, you can run the following commands in the terminal:

```
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

```

Note for Ubuntu users: If apt is unable to find the package, try adding the universe entry to the sources.list file as shown below:

```
sudo vi /etc/apt/sources.list

```

Then, copy the first line `deb http://archive.ubuntu.com/ubuntu bionic main` and paste it as shown below on the next line. If you are using a different release of Ubuntu, replace "bionic" with the respective release name.

```
deb http://archive.ubuntu.com/ubuntu bionic universe

```