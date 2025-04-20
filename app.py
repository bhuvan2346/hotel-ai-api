from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def book_hotel_room():
    data = request.json
    guest_name = data.get('guest_name')
    phone_number = data.get('phone_number')
    check_in_date = data.get('check_in_date')
    check_out_date = data.get('check_out_date')
    room_type = data.get('room_type')
    num_guests = data.get('num_guests')
    special_requests = data.get('special_requests')

    print(f"Booking received for {guest_name} - Phone: {phone_number}")

    return jsonify({
        "message": f"Room booked successfully for {guest_name} from {check_in_date} to {check_out_date}."
    })

if __name__ == '__main__':
    app.run(debug=True)