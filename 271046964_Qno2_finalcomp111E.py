#QUESTION NO 2:

class Property:
    def __init__(self,property_id,name,location,description,rate_pernight):
        
        self.name=name
        self.location=location
        self.description=description
        self.rate_pernight=rate_pernight
        self.avb_status=True
        self.bookings=[]
        
    def is_avb(self,checkin,checkout):
        
        for booking in self.bookings:
            if booking.checkin_date<checkout and booking.check_out_date>checkin:
                return False
            return True
        
class User:
    def __init__(self,user_id,name,contact_details):
        
        self.user_id=user_id
        self.name=name
        self.contact_details=contact_details
        
class Host(User):
    
    def __init__(self,user_id,name,contact_details):
        
        super().__init(user_id,name,contact_details)
        self.properties=[]
        
        
    def list_property(self,property):
        self.properties.append(property)
        
class Guest(User):
    def __init__(self,user_id,name,contact_details):
        
        super().__init(user_id,name,contact_details)
        
        self.bookings=[]
        
    def book_property(self,booking):
        self.bookings.append(booking)
        
        
class Booking:
    def __init__(self,booking_id,property,guest,checkin_date_s,checkout_date_s):
        
        self.booking_id=booking_id
        self.property=property
        self.guest=guest
        self.checkin_date_s=checkin_date_s
        self.checkout_date_s=checkout_date_s
        
        self.booking_status="BOOKING CONFIRMED!"
        
    self.property.update_avb(False)

    def cancel_booking(self):
        
        self.booking_status="BOOKING CANCELED!"

    self.property.update_avb(False)

class Reviews:
    
    def __init__(self,review_id,property,guest,ratings,comment):
        
        self.review_id=review_id
        self.property=property
        self.guest=guest
        self.ratings=ratings
        self.comment=comment
        
if __name__=="__main__":
    
    my_host=Host(user_id=12,name="Laiba",contact_details="Laiba212@gmail.com")
    my_property=Property(property_id=564,name="New villas",locatiion="Lahore",description="Cozy and Secure environment!",rate_pernight=160)
    
    
    host.list_property(booking)
        
    my_guest=Guest(user_id=23,name="Ariel",contact_details="Ariel.2322@gmail.com")
    
    my_booking=Booking(book_id=1037,property=property,guest=guest,checkin_date_s="2024-07-01",checkout_date_s="2024-08-02")
    
    guest.book_property(booking)
    
print(property.avb_status)

booking.cancel_booking()

print(property.avb_status)