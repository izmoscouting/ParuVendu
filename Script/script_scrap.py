{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "36645cfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pandas as pd\n",
    "import re\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "69e6e19c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Launch get_pages(int) to launch the program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "93e14d07",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Lists which will store our datas during the script work, initialize them before launch program\n",
    "pages=[]\n",
    "emp=[]\n",
    "price=[]\n",
    "areas=[]\n",
    "type_h=[]\n",
    "description=[]\n",
    "pieces_nb=[]\n",
    "urls=[]\n",
    "code = []\n",
    "dep=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "013a6c3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Allows us to split zip_code from the emplacement\n",
    "def zip_code(x):\n",
    "    m=[]\n",
    "    n=[]\n",
    "    for c in x:\n",
    "        m.append(re.findall('\\s\\d{1,2}|\\(\\d{2}\\)|\\(\\d+\\)',c))\n",
    "     \n",
    "    \n",
    "    for c in m:\n",
    "        n.append(str(''.join(c)))\n",
    "   \n",
    "\n",
    "    for s in n:\n",
    "        code.append(s.replace('(','').replace(')','').replace(' ',''))\n",
    "        \n",
    "\n",
    "        \n",
    "    for i in range(len(code)):\n",
    "        if code[i] == '1':\n",
    "            code[i] = '75001'\n",
    "        if code[i] == '2':\n",
    "            code[i] = '75002'\n",
    "        if code[i] == '3':\n",
    "            code[i] = '75003'\n",
    "        if code[i] == '4':\n",
    "            code[i] = '75004'\n",
    "        if code[i] == '5':\n",
    "            code[i] = '75005'\n",
    "        if code[i] == '6':\n",
    "            code[i] = '75006'\n",
    "        if code[i] == '7':\n",
    "            code[i] = '75007'\n",
    "        if code[i] == '8':\n",
    "            code[i] = '75008'\n",
    "        if code[i] == '9':\n",
    "            code[i] = '75009'\n",
    "        if code[i] == '10':\n",
    "            code[i] = '75010'\n",
    "        if code[i] == '11':\n",
    "            code[i] = '75011'\n",
    "        if code[i] == '12':\n",
    "            code[i] = '75012'\n",
    "        if code[i] == '13':\n",
    "            code[i] = '75013'\n",
    "        if code[i] == '14':\n",
    "            code[i] = '75014'\n",
    "        if code[i] == '15':\n",
    "            code[i] = '75015'\n",
    "        if code[i] == '16':\n",
    "            code[i] = '75016'\n",
    "        if code[i] == '17':\n",
    "            code[i] = '75017'\n",
    "        if code[i] == '18':\n",
    "            code[i] = '75018'\n",
    "        if code[i] == '19':\n",
    "            code[i] = '75019'\n",
    "        if code[i] == '20':\n",
    "            code[i] = '75020'\n",
    "\n",
    "            \n",
    "#Create the departements\n",
    "def dep_(x):\n",
    "    z = []\n",
    "    a = []\n",
    "    for i in x:\n",
    "        z.append(re.findall('^\\d{2}',i))\n",
    "    for i in z:\n",
    "        dep.append(str(''.join(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "391a3408",
   "metadata": {},
   "outputs": [],
   "source": [
    "def na_to_np(x,y) :\n",
    "    x[y] = x[y].replace('NaN',np.NaN)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fbf015c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Script that will convert our lists into dataframe and csv\n",
    "\n",
    "def lists_to_df(a,b,c,d,e,f,g,h):\n",
    "    names = ['Type', 'Nombre de Pièces', 'Surface (m²)','Prix (€)','Departement','Code Postal','Emplacement', 'Description']\n",
    "    immo = pd.DataFrame(columns = names)\n",
    "    \n",
    "    immo['Type'] = a\n",
    "    immo['Nombre de Pièces'] = b\n",
    "    immo['Surface (m²)'] = c\n",
    "    immo['Prix (€)'] = d\n",
    "    immo['Departement'] = e\n",
    "    immo['Code Postal'] = f\n",
    "    immo['Emplacement'] = g\n",
    "    immo['Description'] = h\n",
    "    \n",
    "    na_to_np(immo,'Nombre de Pièces')\n",
    "    na_to_np(immo,'Code Postal')\n",
    "    na_to_np(immo,'Surface (m²)')\n",
    "    na_to_np(immo,'Departement')\n",
    "    na_to_np(immo,'Type')\n",
    "    na_to_np(immo,'Description')\n",
    "    na_to_np(immo,'Emplacement')\n",
    "    na_to_np(immo,'Prix (€)')\n",
    "    \n",
    "    immo = immo.dropna()\n",
    "    immo = immo.drop_duplicates()\n",
    "    immo = immo.fillna(0)\n",
    "    \n",
    "    immo.to_csv('ParuVendu.csv', index = False, header = True)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4dc47969",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Parse and clean data\n",
    "def parse_pages(x, soup) :\n",
    "    #This variable allows us to fill the unreachables values and have lists of same length to convert them into dataframe later\n",
    "    bot = 'NaN'\n",
    "    \n",
    "    \n",
    "    #This variables will be used in loops to help us select data we need\n",
    "    prices = soup.find_all('div', class_='ergov3-priceannonce')\n",
    "    title = soup.find_all('div', class_=\"ergov3-h3\")\n",
    "    desc = soup.find_all('p',class_='txt-long')\n",
    "    \n",
    "    #Box where we store all type of houses available\n",
    "    model_title = 'Appartement|Maison|Hôtel|T2|T3|T1|T4|T5|T6|Duplex/triplex|Loft|Villa|Atelier|studio'\n",
    "    \n",
    "    #Avoid local variable error\n",
    "    global i\n",
    "    \n",
    "    #Loop to reach and clean real estate prices data\n",
    "    for p in prices :\n",
    "        price.append((p.text.replace(\"€\", \"\").replace(\"\\r\",\"\").replace(\"\\n\",\"\").replace('*','').replace(\" \", \"\")))\n",
    "            \n",
    "    #Reaching Cities names and zip codes        \n",
    "    for c in title:\n",
    "        if c.find('cite'):\n",
    "            emp.append(c.find('cite').text.replace('\\r','').replace('\\n','').replace(\"\\t\",\"\"))\n",
    "        else:\n",
    "            emp.append(bot)\n",
    "\n",
    "    #Reaching houses type \n",
    "    for t in title:\n",
    "        \n",
    "        if t.find('span'):\n",
    "            for i in re.findall(model_title, t.find('span').text):\n",
    "                type_h.append(i)\n",
    "            if i not in re.findall(model_title, t.find('span').text):\n",
    "                type_h.append(bot)\n",
    "    \n",
    "    #Reaching number of pieces in a house\n",
    "    for b in title :\n",
    "\n",
    "        if b.find('span'):\n",
    "            \n",
    "            for i in re.findall('\\n[0-9]{1,2}| [0-9]{1,2} p|[0-9]{1,2}p', b.text):\n",
    "                \n",
    "                pieces_nb.append(int(i.replace(' p','').replace('\\n','').replace(\"p\",\"\")))\n",
    "                \n",
    "            if i not in re.findall('\\n[0-9]{1,2}| [0-9]{1,2} p|[0-9]{1,2}p', b.text):\n",
    "                pieces_nb.append(bot)\n",
    "   \n",
    "    #Reaching areas of houses            \n",
    "    for b in title:\n",
    "        if b.find('span'):\n",
    "            for i in (re.findall('[0-9]+ m|[0-9]+m', b.text)):\n",
    "                areas.append(i.replace(' m','').replace('m',''))\n",
    "                \n",
    "            if i not in (re.findall('[0-9]+ m|[0-9]+m', b.text)) :\n",
    "                areas.append(bot) \n",
    "        \n",
    "        \n",
    "\n",
    "    #Reaching descriptions of houses\n",
    "    for d in desc:\n",
    "        description.append(d.text.replace(\"\\r\",\"\").replace(\"\\n\",\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "517ea4b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function to change pages\n",
    "def get_pages(count=int):\n",
    "    for pages_nb in range(1,count+1):\n",
    "        url = f\"https://www.paruvendu.fr/immobilier/annonceimmofo/liste/listeAnnonces?%20tt=1&at=1&nbp0=99&pa=FR&lo=75,77,78,91,92,93,94,95&lol=0&ray=50&p={pages_nb}\"\n",
    "        urls.append(url)\n",
    "    loop_pages(urls,emp,code)\n",
    "    \n",
    "\n",
    "#Script where we put urls list to enable all the functions\n",
    "\n",
    "#x stands for urls, y for emp and z for code\n",
    "def loop_pages(x,y,z):\n",
    "    for n in range(len(x)):\n",
    "        page = requests.get(x[n])\n",
    "        soup = bs(page.content, 'html.parser')\n",
    "        parse_pages(x[n], soup)\n",
    "        pages.append(page)\n",
    "    zip_code(y)\n",
    "    dep_(z)\n",
    "    lists_to_df(type_h,pieces_nb,areas,price,dep,code,emp,description)\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ed36a52a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Launch program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f38adde8",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_pages()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2dc6814a",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "#All the code below can be used to check the datas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19775eef",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(emp),len(price),len(areas),len(type_h),len(description),len(pieces_nb),len(code),len(dep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41d8e5a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(pieces_nb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11b860a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "502f5c60",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa4adfca",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(areas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15275130",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(type_h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16850a3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(urls)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}