class DynamicArray {
public:
int *dynarr;
int cap;
int end;
    DynamicArray(int capacity): cap(1), end(0) {
        cap = capacity;
        dynarr = new int[capacity];
    }

    int get(int i) {
        return dynarr[i];
    }

    void set(int i, int n) {
        dynarr[i] = n;
    }

    void pushback(int n) {
        if (end == cap) {
            resize();
        }
        dynarr[end++] = n;
    }

    int popback() {
        end--;
        return dynarr[end];
    }

    void resize() {
        int i = 0;
        int tempcap = cap*2;
        int *temp = new int[tempcap];
        while(i < end) {
            temp[i] = dynarr[i];
            i++;
        }
        delete[] dynarr;
        cap = tempcap;
        dynarr = temp;
    }

    int getSize() {
        return end;
    }

    int getCapacity() {
        return cap;
    }
};
