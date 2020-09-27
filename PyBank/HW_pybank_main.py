{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Month: 86\n",
      "Total: 38382578\n",
      "Average Change: $-2315.1176470588234\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "def average(changes):\n",
    "    result = sum(changes)/len(changes)\n",
    "    return (f'Average Change: ${result}')\n",
    "\n",
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
