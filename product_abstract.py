from abc import ABC, abstractmethod


class Product:
    product_name = ""
    product_Id = ""
    product_Image = ""


class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product: Product):
        pass

    @abstractmethod
    def get_product_by_id(self, product_Id: Product):
        pass

    @abstractmethod
    def upload_product_image(self, product_Image: Product):
        pass

    @abstractmethod
    def delete_product(self, product: Product):
        pass


class ProductManager(ProductAbstract):
    def create_product(self, name: Product):
        print(f"Product: {name}")

    def upload_product_image(self, product_Image):
        print(product_Image)

    def edit_product(self):
        print("Product edition")

    def get_product_by_id(self, product_Id):
        print(product_Id)

    def delete_product(self):
        print("Product deletion")


product_m = ProductManager()
product_m.upload_product_image("Image of the Product")
product_m.edit_product()
product_m.create_product("Peas")
product_m.upload_product_image("20010D")
product_m.delete_product()
