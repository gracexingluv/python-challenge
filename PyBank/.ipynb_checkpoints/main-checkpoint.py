{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data= os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def average(changes):\n",
    "    length = len(changes)\n",
    "    total = 0.0\n",
    "    for x in changes:\n",
    "        total += x\n",
    "        result = round(total/length,2)\n",
    "    return (f'Average Change: ${result}')\n",
    "\n",
    "Total = 0\n",
    "numbers =[]\n",
    "months = []\n",
    "changes = []\n",
    "\n",
    "with open(budget_data,\"r\") as file:\n",
    "    csv_reader_budget = csv.reader(file, delimiter=\",\")\n",
    "    next(csv_reader_budget, None) \n",
    "    for row in csv_reader_budget:\n",
    "        Total += float(row[1])\n",
    "        numbers.append(int(row[1]))\n",
    "        months.append(row[0])\n",
    "        \n",
    "changes = [int(numbers[n])-int(numbers[n-1]) for n in range(1,len(numbers))]  \n",
    "months_max = months[changes.index(max(changes))+1]\n",
    "months_min = months[changes.index(min(changes))+1]\n",
    "\n",
    "print(f'Total Month: {len(months)}')\n",
    "print(f'Total: {int(Total)}')   \n",
    "print(average(changes))\n",
    "print(f'Greatest Increase in Profits: {months_max} (${max(changes)})')\n",
    "print(f'Greatest Decrease in Profits: {months_min} (${min(changes)})')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
