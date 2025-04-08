def quicksort(sequence):

        #quando la lista ha lunghezza 1 o 0 (quando ha lunghezza 0 puoi anche non tornanare nulla
    if len(sequence) == 1:
         return sequence
    else:
        pivot = sequence[0] #a caso scegli tanto non sai nulla sull'ordine
        #adesso devi dividere la sequenza in sottosequenze
        # sequence_smaller=[]
        # sequence_larger=[]
        # sequence_pivot=[]
        # for i in sequence:
        #     if i < pivot:
        #         sequence_smaller.append(i)
        #     elif i > pivot:
        #         sequence_larger.append(i)
        #     else:
        #         sequence_pivot.append(i)

        sequenza_smaller=[n for n in sequence if n<pivot]
        sequenza_larger=[n for n in sequence if n>pivot]
        sequenza_pivot=[n for n in sequence if n==pivot]
        return (quicksort(sequenza_smaller)+sequenza_pivot+quicksort(sequenza_larger))


if __name__ == '__main__':
    sequence= [3,5,2,9,11,4,7]
    print(quicksort(sequence))