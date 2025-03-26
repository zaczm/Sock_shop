# Import the function to test 
from app import get_available_products, get_product_by_id, get_all_categories

#Test the get available product fucntion
def test_get_available_products():
    # Verify that we can retrieve products 
    # Call the get_available_product function
    product = get_available_products()

    # Test using an assertion if three product were returned 
    assert len(product) == 3

    # Test that product have all of the required fields
    assert all('id' in p and 'image' in p and 'category' in p and 
               'base_price' in p and 'description' in p and 'name' in p
               for p in product)
    
    # Test that the number of products in the 'funny' category equals two
    assert len(get_available_products('funny')) == 2

# Test the get product by id function
def test_get_product_by_id():
    # Get a product from the  collection of products withe the product id 1
    product = get_product_by_id(1)

    # Test that the product exists and that the ID is 1 and the name is Meme Lord
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'

    # Test that an invalid product id is handled gracefully instead of throwing an error
    assert get_product_by_id(999) is None

# Test the get all categories function
def test_get_all_categories():
    # Get the categories of socks
    categories = get_all_categories()
    # Test that there are two categories in the list
    assert len(categories) == 2
    # Test that the two categories are funny and school
    assert 'funny' in categories and 'school' in categories