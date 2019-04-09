import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('shanks-18d6d-firebase-adminsdk-lgquf-adc900e6a1.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://shanks-18d6d.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
        'boxes': 
            {
                'box001': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
        })

# update data
ref = db.reference('boxes')
box_ref = ref.child('box001')
box_ref.update({
    'color': 'blue'
})

ref = db.reference('boxes')
ref.update({
    'box001/color': 'red',
    'box002/color': 'blue'
})

ref = db.reference('boxes')
ref.push({
    'color': 'purple',
    'width': 7,
    'height': 8,
    'length': 6
})


ref = db.reference('boxes')
# Generate a reference to a new location and add some data using push()
new_box_ref = ref.push({
    'color': 'purple',
    'width': 7,
    'height': 8,
    'length': 6
})
# Get the unique key generated by push()
box_id = new_box_ref.key

# retrive Data

ref = db.reference('boxes')
print(ref.get())