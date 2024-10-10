from flask import Blueprint, request, url_for, redirect, render_template

transaction_bp = Blueprint("transaction_bp", __name__, template_folder='templates', static_folder='static')

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@transaction_bp.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions, balance=total_balance())

# Create operation
@transaction_bp.route("/add",methods=["GET","POST"])
def add_transaction():
    if request.method=='GET':
        return render_template("form.html")
    transaction = {'id': len(transactions)+1,
                   'date': request.form['date'],
                   'amount': float(request.form['amount'])
                   }
    transactions.append(transaction)
    return redirect(url_for("transaction_bp.get_transactions"))

# Update operation
@transaction_bp.route("/edit/<int:transaction_id>",methods=["GET","POST"])
def edit_transaction(transaction_id):
    if request.method=='GET':
        for transaction in transactions:
            if transaction['id']==transaction_id:
                return render_template("edit.html",transaction=transaction)
        return "transaction not found.", 404
    date=request.form['date']
    amount=float(request.form['amount'])
    for transaction in transactions:
        if transaction['id']==transaction_id:
            transaction['date']=date
            transaction['amount']=amount
            break
    return redirect(url_for("transaction_bp.get_transactions"))

# Delete operation
@transaction_bp.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction_id==transaction['id']:
            transactions.remove(transaction)
            return redirect(url_for("transaction_bp.get_transactions"))
    return "transaction not found", 404
    
#search operation
@transaction_bp.route("/search", methods=['GET','POST'])
def search_transactions():
    if request.method=='POST':
        min=float(request.form['min_amount'])
        max=float(request.form['max_amount'])
        filtered_transactions=[transaction for transaction in transactions if (transaction['amount']<=max and transaction['amount']>=min)]
        return render_template("transactions.html", transactions=filtered_transactions)
    return render_template("search.html")

#total balance calculation
@transaction_bp.route("/balance")
def total_balance():
    balance=sum([transaction['amount'] for transaction in transactions])
    return f"Total Balance: {balance}"