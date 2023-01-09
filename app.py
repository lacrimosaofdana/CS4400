import os
import sys
import pymysql

from flask import Flask, render_template, flash, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:plokijQAZWSXEDC1009@127.0.0.1:3306/restaurant_supply_express'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/add/owners', methods=['GET', 'POST'])
def add_owners():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_first_name = request.form.get('first_name')
        ip_last_name = request.form.get('last_name')
        ip_address = request.form.get('address')
        ip_birthdate = request.form.get('birthdate')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_owner', (ip_username, ip_first_name, ip_last_name, ip_address, ip_birthdate))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_owners'))

    return render_template('add_owners.html')


# 2
@app.route('/add/employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_first_name = request.form.get('first_name')
        ip_last_name = request.form.get('last_name')
        ip_address = request.form.get('address')
        ip_birthdate = request.form.get('birthdate')
        ip_taxID = request.form.get('taxID')
        ip_hired = request.form.get('hired_date')
        ip_employee_experience = request.form.get('employee_experience')
        ip_salary = request.form.get('salary')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_employee', (
        ip_username, ip_first_name, ip_last_name, ip_address, ip_birthdate, ip_taxID, ip_hired, ip_employee_experience,
        ip_salary))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_employee'))

    return render_template('add_employee.html')


# 3
@app.route('/add/pilot/role', methods=['GET', 'POST'])
def add_pilot_role():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_licenseID = request.form.get('licenseID')
        ip_pilot_experience = request.form.get('pilot_experience')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_pilot_role', (ip_username, ip_licenseID, ip_pilot_experience))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_pilot_role'))

    return render_template('add_pilot_role.html')


# 4
@app.route('/add/worker/role', methods=['GET', 'POST'])
def add_worker_role():
    if request.method == 'POST':
        ip_username = request.form.get('username')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_worker_role', [ip_username])

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_worker_role'))

    return render_template('add_worker_role.html')


# 5
@app.route('/add/ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        ip_barcode = request.form.get('barcode')
        ip_iname = request.form.get('ingredient_name')
        ip_weight = request.form.get('weight')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_ingredient', (ip_barcode, ip_iname, ip_weight))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_ingredient'))
    return render_template('add_ingredient.html')


# 6
@app.route('/add/drone', methods=['GET', 'POST'])
def add_drone():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_fuel = request.form.get('fuel')
        ip_capacity = request.form.get('capacity')
        ip_sales = request.form.get('sales')
        ip_flown_by = request.form.get('flown_by')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_drone', (ip_id, ip_tag, ip_fuel, ip_capacity, ip_sales, ip_flown_by))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_drone'))
    return render_template('add_drone.html')


# 7
@app.route('/add/restaurant', methods=['GET', 'POST'])
def add_restaurant():
    if request.method == 'POST':
        ip_long_name = request.form.get('long_name')
        ip_rating = request.form.get('rating')
        ip_spent = request.form.get('spent')
        ip_location = request.form.get('location')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_restaurant', (ip_long_name, ip_rating, ip_spent, ip_location))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_restaurant'))
    return render_template('add_restaurant.html')


# 8
@app.route('/add/service', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_long_name = request.form.get('long_name')
        ip_home_base = request.form.get('home_base')
        ip_manager = request.form.get('manager')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_service', (ip_id, ip_long_name, ip_home_base, ip_manager))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_service'))

    return render_template('add_service.html')


# 9
@app.route('/addlocation', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        ip_label = request.form.get('label')
        ip_xcoord = request.form.get('xcoord')
        ip_ycoord = request.form.get('ycoord')
        ip_space = request.form.get('space')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('add_location', (ip_label, ip_xcoord, ip_ycoord, ip_space))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('add_location'))

    return render_template('add_location.html')


# 10
@app.route('/startfund', methods=['GET', 'POST'])
def start_fund():
    if request.method == 'POST':
        ip_owner = request.form.get('owner')
        ip_long_name = request.form.get('longname')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('start_funding', (ip_owner, ip_long_name))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('start_fund'))

    return render_template('start_funding.html')


# 11
@app.route('/hire/employee', methods=['GET', 'POST'])
def hire_employee():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_id = request.form.get('id')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('hire_employee', (ip_username, ip_id))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('hire_employee'))

    return render_template('hire_employee.html')


# 12
@app.route('/fire/employee', methods=['GET', 'POST'])
def fire_employee():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_id = request.form.get('id')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('fire_employee', (ip_username, ip_id))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('fire_employee'))

    return render_template('fire_employee.html')


# 13
@app.route('/manage/service', methods=['GET', 'POST'])
def manage_service():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_id = request.form.get('id')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('manage_service', (ip_username, ip_id))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('manage_service'))
    return render_template('manage_service.html')


# 14
@app.route('/takeoverdrones', methods=['GET', 'POST'])
def take_over_drones():
    if request.method == 'POST':
        ip_username = request.form.get('username')
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('takeover_drone', (ip_username, ip_id, ip_tag))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('take_over_drones'))

    return render_template('takeover_drone.html')


# 15
@app.route('/joinswarm', methods=['GET', 'POST'])
def join_swarm():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_swarm_leader_tag = request.form.get('swarm_tag')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('join_swarm', (ip_id, ip_tag, ip_swarm_leader_tag))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('join_swarm'))

    return render_template('join_swarm.html')


# 16
@app.route('/leaveswarm', methods=['GET', 'POST'])
def leave_swarm():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_swarm_tag = request.form.get('swarm_tag')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('leave_swarm', (ip_id, ip_swarm_tag))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('leave_swarm'))

    return render_template('leave_swarm.html')


# 17
@app.route('/load/drone', methods=['GET', 'POST'])
def load_drone():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_barcode = request.form.get('barcode')
        ip_more_packages = request.form.get('more_packages')
        ip_price = request.form.get('price')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('load_drone', (ip_id, ip_tag, ip_barcode, ip_more_packages, ip_price))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('load_drone'))
    return render_template('load_drone.html')


# 18
@app.route('/refuel/drone', methods=['GET', 'POST'])
def refuel_drone():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_more_fuel = request.form.get('more_fuel')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('refuel_drone', (ip_id, ip_tag, ip_more_fuel))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('refuel_drone'))
    return render_template('refuel_drone.html')


# 19
@app.route('/flydrone', methods=['GET', 'POST'])
def fly_drone():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_destination = request.form.get('destination')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('fly_drone', (ip_id, ip_tag, ip_destination))

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('fly_drone'))

    return render_template('fly_drone.html')


# 20
@app.route('/purchase/ingredient', methods=['GET', 'POST'])
def purchase_ingredient():
    if request.method == 'POST':
        ip_long_name = request.form.get('long_name')
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        ip_barcode = request.form.get('barcode')
        ip_quantity = request.form.get('quantity')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('purchase_ingredient', (ip_long_name, ip_id, ip_tag, ip_barcode, ip_quantity))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('purchase_ingredient'))
    return render_template('purchase_ingredient.html')


# 21
@app.route('/remove/ingredient', methods=['GET', 'POST'])
def remove_ingredient():
    if request.method == 'POST':
        ip_barcode = request.form.get('barcode')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('remove_ingredient', [ip_barcode])
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('remove_ingredient'))
    return render_template('remove_ingredient.html')


# 22
@app.route('/remove/drone', methods=['GET', 'POST'])
def remove_drone():
    if request.method == 'POST':
        ip_id = request.form.get('id')
        ip_tag = request.form.get('tag')
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('remove_drone', (ip_id, ip_tag))
        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('remove_drone'))
    return render_template('remove_drone.html')


# 23
@app.route('/remove/pilot/role', methods=['GET', 'POST'])
def remove_pilot_role():
    if request.method == 'POST':
        ip_username = request.form.get('username')

        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('remove_pilot_role', [ip_username])

        if cursor.rowcount > 0:
            flash('Item updated.', 'success')
        else:
            flash('Invalid input.', 'danger')
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('remove_pilot_role'))

    return render_template('remove_pilot_role.html')


# 24
@app.route('/display_owner_view', methods=['GET', 'POST'])
def display_owner_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_owner_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_owner_view.html', results=results)


# 25
@app.route('/display_employee_view', methods=['GET', 'POST'])
def display_employee_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_employee_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_employee_view.html', results=results)


# 26
@app.route('/display_pilot_view', methods=['GET', 'POST'])
def display_pilot_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_pilot_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_pilot_view.html', results=results)


# 27
@app.route('/display_location_view', methods=['GET', 'POST'])
def display_location_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_location_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_location_view.html', results=results)


# 28
@app.route('/display_ingredient_view', methods=['GET', 'POST'])
def display_ingredient_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_ingredient_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_ingredient_view.html', results=results)


# 29
@app.route('/display_service_view', methods=['GET', 'POST'])
def display_service_view():
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from display_service_view')
    results = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('display_service_view.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
