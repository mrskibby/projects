import os
import pandas as pd
import ast
import matplotlib.pyplot as plt
import webbrowser
import numpy as np


from model_product import Product

class ProductOperation(Product):
    product_url = "data/products.txt"
    product_files = "data/product"

    def extract_products_from_files(self):
        product_data = []

        # Get the list of csv files in the data/product directory
        file_list = [file for file in os.listdir("data/product") if file.endswith(".csv")]

        # Read each csv file and extract the necessary data
        for file_name in file_list:
            file_path = os.path.join("data/product", file_name)
            df = pd.read_csv(file_path)

            # Extract the required columns from the DataFrame
            for _, row in df.iterrows():
                pro_id = row['id']
                pro_model = row['model']
                pro_category = row['category']
                pro_name = row['name'].replace(',', '')  # Remove commas from pro_name
                pro_current_price = row['current_price']
                pro_raw_price = row['raw_price']
                pro_discount = row['discount']
                pro_likes_count = row['likes_count']

                product_data.append({
                    "pro_id": str(pro_id),
                    "pro_model": str(pro_model),
                    "pro_category": str(pro_category),
                    "pro_name": str(pro_name),
                    "pro_current_price": str(pro_current_price),
                    "pro_raw_price": str(pro_raw_price),
                    "pro_discount": str(pro_discount),
                    "pro_likes_count": str(pro_likes_count)
                })

        # Save the extracted product data into the data/products.txt file
        with open("data/products.txt", "w", encoding="utf-8") as file:
            for product in product_data:
                file.write(str(product) + "\n")

    def get_product_list(self, page_number):
        try:
            products_per_page = 10
            total_pages = 0
            product_list = []

            # Read the product data from the file
            with open(self.product_url, "r") as file:
                lines = file.readlines()
                total_products = len(lines)
                total_pages = (total_products - 1) // products_per_page + 1

                if page_number > total_pages:
                    print(f"There is no page number: {page_number}. Total Pages: {total_pages}")
                else:
                    # Calculate the start and end indices of the products for the given page
                    start_index = (page_number - 1) * products_per_page
                    end_index = min(start_index + products_per_page, total_products)

                    # Extract the products for the given page
                    for line in lines[start_index:end_index]:
                        product_dict = eval(line)  # Convert the string representation of dictionary to a dictionary object
                        product = Product(product_dict["pro_id"], product_dict["pro_model"],
                                          product_dict["pro_category"],
                                          product_dict["pro_name"], product_dict["pro_current_price"],
                                          product_dict["pro_raw_price"],
                                          product_dict["pro_discount"], product_dict["pro_likes_count"])
                        product_list.append(line.strip('\n'))
            # print(f"{product_list}, {page_number}, {total_pages}")
            # print(total_products)
            return product_list, page_number, total_pages
        except IOError:
            return None, None, None

    def delete_product(self, product_id):
        with open(self.product_url, 'r') as file:
            lines = file.readlines()
        found_product = False
        with open(self.product_url, 'w') as file:
            for line in lines:
                product_data = ast.literal_eval(line)
                if product_data['pro_id'] != product_id:
                    file.write(line)
                else:
                    found_product = True
        if not found_product:
            print("Product could not be found")
        else:
            print("Product deleted successfully")

    def get_product_list_by_keyword(self, keyword):
        try:
            product_list = []
            page_number = 0

            # Read the product data from the file
            with open(self.product_url, "r") as file:
                lines = file.readlines()

                # Extract the products whose name contains the keyword
                for line in lines:
                    product_dict = eval(line)  # Convert the string representation of dictionary to a dictionary object
                    product_name = product_dict["pro_name"]
                    if keyword.lower() in product_name.lower():
                        product = Product(product_dict["pro_id"], product_dict["pro_model"], product_dict["pro_category"],
                                          product_name, product_dict["pro_current_price"], product_dict["pro_raw_price"],
                                          product_dict["pro_discount"], product_dict["pro_likes_count"])
                        product_list.append(line.strip('\n'))
            # print(product_list)
            return product_list
        except IOError:
            return None

    def get_product_by_id(self, product_id):
        try:
            product_list = []

            # Read the product data from the file
            with open(self.product_url, "r") as file:
                lines = file.readlines()

                # Extract the products whose name contains the keyword
                for line in lines:
                    product_dict = eval(line)  # Convert the string representation of dictionary to a dictionary object
                    product_name = product_dict["pro_id"]
                    if product_id in product_name:
                        product = Product(product_dict["pro_id"], product_dict["pro_model"], product_dict["pro_category"],
                                          product_name, product_dict["pro_current_price"], product_dict["pro_raw_price"],
                                          product_dict["pro_discount"], product_dict["pro_likes_count"])
                        product_list.append(line.strip('\n'))
            # print(product_list)
            return product_list
        except IOError:
            return None

    def generate_category_figure(self):
        # Read the product data from the file
        df = pd.read_csv("data/products.txt", sep=",", header=None)
        df.columns = ["pro_id", "pro_model", "pro_category", "pro_name", "pro_current_price",
                      "pro_raw_price", "pro_discount", "pro_likes_count"]

        # Group the products by category and count the number of products in each category
        category_counts = df["pro_category"].value_counts().sort_values(ascending=False)

        # Create the bar chart
        fig, ax = plt.subplots(figsize=(10, 8))
        category_counts.plot(kind="bar", ax=ax)

        # Set the labels and title
        ax.set_xlabel("Category")
        ax.set_ylabel("Number of Products")
        ax.set_title("Total Number of Products by Category")

        # Save the figure
        figure_path = os.path.join("data", "figure", "category_figure.png")
        plt.savefig(figure_path)

        # Show the figure in a browser window
        webbrowser.open("file://" + os.path.abspath(figure_path))

        plt.close(fig)

        print("The figure for the category is saved in the figure folder")

    def generate_discount_figure(self):
        less_than_30 = 0
        between_30_and_60 = 0
        greater_than_60 = 0

        # Read the product data from the file
        with open(self.product_url, "r", encoding="utf-8") as file:
            product_lines = file.readlines()

        for line in product_lines:
            product_data = eval(line)
            discount = float(product_data["pro_discount"])
            if discount < 30:
                less_than_30 += 1
            elif discount >= 30 and discount <= 60:
                between_30_and_60 += 1
            else:
                greater_than_60 += 1

        # Assign different name for different sections in pie chart
        labels = ["< 30%", "30% - 60%", "> 60%"]

        # Assign the value of size to pie chart
        sizes = [less_than_30, between_30_and_60, greater_than_60]

        # Create the pie chart with different colors for each discount range
        colors = ["#FF7F0E", "#1F77B4", "#FF1493"]

        plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
        plt.axis("equal")

        # Set the title
        plt.title("Proportion of Products by Discount Range")

        # Save the figure
        figure_path = os.path.join("data", "figure", "discount_figure.png")
        plt.savefig(figure_path)

        # Show the figure in a browser window
        webbrowser.open("file://" + os.path.abspath(figure_path))

        plt.close()

        print("The figure for the discount is saved in the figure folder")

    def generate_likes_count_figure(self):
        category_likes = {}

        with open("data/products.txt", "r", encoding="utf-8") as file:
            product_lines = file.readlines()

        for line in product_lines:
            product_data = eval(line)
            category = product_data["pro_category"]
            likes_count = int(product_data["pro_likes_count"])

            if category in category_likes:
                category_likes[category] += likes_count
            else:
                category_likes[category] = likes_count

        sorted_categories = sorted(category_likes.items(), key=lambda x: x[1])
        # for i in range(len(category)-1):
        categories = [category[0] for category in sorted_categories]
        likes_counts = [category[1] for category in sorted_categories]

        plt.barh(categories, likes_counts)
        plt.xlabel("Likes Count")
        plt.ylabel("Category")
        plt.title("Sum of Likes Count for Each Category")
        plt.tight_layout()

        figure_path = "data/figure/likes_count_figure.png"
        plt.savefig(figure_path)

        # Show the figure in a browser window
        webbrowser.open("file://" + os.path.abspath(figure_path))

        plt.close()

    def generate_discount_likes_count_figure(self):
        discount_values = []
        likes_counts = []

        with open("data/products.txt", "r", encoding="utf-8") as file:
            product_lines = file.readlines()

        for line in product_lines:
            product_data = eval(line)
            if "pro_discount" in product_data and product_data["pro_discount"]:
                discount_values.append(float(product_data["pro_discount"]))
                likes_counts.append(int(product_data["pro_likes_count"]))

        plt.scatter(discount_values, likes_counts)
        plt.xlabel("Discount")
        plt.ylabel("Likes Count")
        plt.title("Relationship between Likes Count and Discount")
        plt.tight_layout()

        figure_path = "data/figure/discount_likes_count_figure.png"
        plt.savefig(figure_path)

        # Show the figure in a browser window
        webbrowser.open("file://" + os.path.abspath(figure_path))

        plt.close()

    def delete_all_products(self):
        # Open the file in write mode, which clears all existing content
        with open("data/products.txt", "w") as file:
            pass


# test = ProductOperation()
# test.extract_products_from_files() #correct
# test.get_product_list(1) #not correct but working
# test.delete_product('1671872') #correct
# test.get_product_list_by_keyword('Nail') #correct by not returning object
# test.get_product_by_id('1674377') #correct by not returning object
# test.generate_category_figure() # correct
# test.generate_discount_figure() # correct
# test.generate_likes_count_figure() #working but not correct
# test.generate_discount_likes_count_figure() #correct
# test.delete_all_products() # correct