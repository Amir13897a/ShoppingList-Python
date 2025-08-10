import os
import json

class ShoppingList:
    def __init__(self, filename="shopping_data.json"):
        self.filename = filename
        self.items = []
        self.load_from_file()  # bargozari khodkar az file

    def add_item(self, name, price):
        """add kardane mahsoole jadid"""
        added_item = {
            'id': len(self.items) + 1,
            'name': name,
            'price': price
        }
        self.items.append(added_item)
        self.save_to_file()
        print(f"✅ mahsul '{name}' ba gheymat {price} ezafe shod")
        
    def remove_item(self, item_id):
        """hazf mahsul bar asas ID"""
        for i, item in enumerate(self.items):
            if item['id'] == item_id:
                removed_item = self.items.pop(i)
                # update ID ha
                for j in range(i, len(self.items)):
                    self.items[j]['id'] = j + 1
                self.save_to_file()
                print(f"❌ mahsul '{removed_item['name']}' hazf shod")
                return True
        print(f"❌ mahsul ba ID {item_id} peyda nashod")
        return False

    def search_items(self, search_term):
        """jostojo dar mahsulat"""
        results = []
        search_term = search_term.lower()
        
        for item in self.items:
            if (search_term in item['name'].lower() or 
                str(search_term) in str(item['price'])):
                results.append(item)
        
        if results:
            print(f"\n🔍 natije jostojo '{search_term}':")
            for item in results:
                print(f"  ID: {item['id']} | {item['name']}: {item['price']}")
        else:
            print(f"🔍 hich mahsuli ba '{search_term}' peyda nashod")
        
        return results

    def total_price(self):
        """mohasebe jam'e gheymat ha"""
        total = sum(item['price'] for item in self.items)
        return total

    def display_all(self):
        """namayesh hameye mahsulat"""
        if not self.items:
            print("📝 list kharid khali ast")
            return
        
        print("\n--- 📋 list kharid ---")
        for item in self.items:
            print(f"  ID: {item['id']} | {item['name']}: {item['price']}")
        print(f"💰 majmooe: {self.total_price()}")

    def save_to_file(self):
        """zakhire dar JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.items, file, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ khata dar zakhire: {e}")

    def load_from_file(self):
        """bargozari az JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.items = json.load(file)
                print(f"📁 file {self.filename} bargozari shod")
            except Exception as e:
                print(f"❌ khata dar bargozari: {e}")
                self.items = []
        else:
            print(f"📁 file jadid {self.filename} ijad khahad shod")

def show_menu():
    """namayesh menuye asli"""
    print("\n" + "="*50)
    print("🛒 system modiriyat list kharid")
    print("="*50)
    print("1. ➕ ezafe kardan mahsul")
    print("2. ❌ hazf mahsul")
    print("3. 🔍 jostojo dar mahsulat")
    print("4. 📋 namayesh hame mahsulat")
    print("5. 💰 namayesh majmooe kol")
    print("6. 💾 zakhire dar file")
    print("7. 🚪 khorooj")
    print("="*50)

def main():
    """tabe asli barname"""
    shopping = ShoppingList()
    
    while True:
        show_menu()
        choice = input("\nentekhab konid (1-7): ").strip()
        
        if choice == '1':
            print("\n--- ➕ ezafe kardan mahsule jadid ---")
            name = input("nam mahsul: ").strip()
            if not name:
                print("❌ nam mahsul nemitavanad khali bashad")
                continue
                
            try:
                price = int(input("gheymat: "))
                if price < 0:
                    print("❌ gheymat nemitavanad manfi bashad")
                    continue
                shopping.add_item(name, price)
            except ValueError:
                print("❌ lotfan gheymat ra be sorat adad vared konid")
                
        elif choice == '2':
            if not shopping.items:
                print("❌ list kharid khali ast")
                continue
                
            print("\n--- ❌ hazf mahsul ---")
            shopping.display_all()
            try:
                item_id = int(input("\nID mahsule mored nazar baraye hazf: "))
                shopping.remove_item(item_id)
            except ValueError:
                print("❌ lotfan ID ra be sorat adad vared konid")
                
        elif choice == '3':
            if not shopping.items:
                print("❌ list kharid khali ast")
                continue
                
            print("\n--- 🔍 jostojo dar mahsulat ---")
            search_term = input("ebarat jostojo: ").strip()
            if search_term:
                shopping.search_items(search_term)
            else:
                print("❌ ebarat jostojo nemitavanad khali bashad")
                
        elif choice == '4':
            shopping.display_all()
            
        elif choice == '5':
            if shopping.items:
                print(f"\n💰 majmooe kol: {shopping.total_price()}")
            else:
                print("📝 list kharid khali ast")
                
        elif choice == '6':
            shopping.save_to_file()
            print("✅ file ba movafaghiat zakhire shod")
            
        elif choice == '7':
            print("\n👋 khodahafez!")
            break
            
        else:
            print("❌ entekhab namotabar! lotfan adad 1 ta 7 ra vared konid")
        
        input("\nbaraye edame Enter bezanid...")

if __name__ == "__main__":
    main()