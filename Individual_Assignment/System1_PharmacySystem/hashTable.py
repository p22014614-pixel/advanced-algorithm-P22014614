from medicine import Medicine


class HashTable:

    def __init__(self, size):
        self.size = size

        # Array structure for buckets
        self.table = [None] * size


    def hash_function(self, key):

        total = 0

        for char in key:
            total += ord(char)

        return total % self.size



    def insert(self, medicine):

        index = self.hash_function(medicine.medicine_id)

        original_index = index


        while self.table[index] is not None:

            index = (index + 1) % self.size


            if index == original_index:
                print("Hash table is full")
                return


        self.table[index] = medicine

        print("Inserted:", medicine.name)



    def search(self, medicine_id):

        index = self.hash_function(medicine_id)

        original_index = index


        while self.table[index] is not None:

            if self.table[index].medicine_id == medicine_id:
                return self.table[index]


            index = (index + 1) % self.size


            if index == original_index:
                break


        return None



    def display(self):

        print("\nPHARMACY INVENTORY")

        for i in range(self.size):

            print("Bucket", i, ":", end=" ")

            if self.table[i] is not None:
                print(self.table[i].name)

            else:
                print("Empty")