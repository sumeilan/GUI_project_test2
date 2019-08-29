def is_element_exist(self, element):
    try:
        if self.driver.find_element_by_id(element):
            return True
        else:
            return False
    except Exception as e:
        print(e)


