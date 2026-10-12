
import json
from pathlib import Path
from datetime import date

import pandas as pd
import streamlit as st


# File to store expenses
DATA_FILE = Path(__file__).with_name("expenses.json")


# Page settings
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# Load expenses from JSON file
def load_expenses():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            st.error("Could not read expenses.json.")
    return []


# Save expenses to JSON file
def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()


# Dashboard heading
st.title("💰 Expense Tracker")
st.caption("Track your spending. Understand your money.")


# Sidebar: Add an expense
with st.sidebar:
    st.header("➕ Add an Expense")

    with st.form("expense_form", clear_on_submit=True):
        amount = st.number_input(
            "Amount (₹)",
            min_value=0.01,
            value=100.0,
            step=10.0
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Shopping",
                "Bills",
                "Education",
                "Entertainment",
                "Other"
            ]
        )

        description = st.text_input("Description")
        expense_date = st.date_input(
            "Date",
            value=date.today()
        )

        submitted = st.form_submit_button(
            "Add Expense",
            use_container_width=True
        )

        if submitted:
            new_expense = {
                "amount": round(amount, 2),
                "category": category,
                "description": description.strip(),
                "date": expense_date.isoformat()
            }

            st.session_state.expenses.append(new_expense)
            save_expenses(st.session_state.expenses)

            st.success("Expense added!")
            st.rerun()


# Display dashboard
expenses = st.session_state.expenses

if expenses:
    df = pd.DataFrame(expenses)

    df["amount"] = pd.to_numeric(df["amount"])
    df["date"] = pd.to_datetime(df["date"])

    # Calculate summary values
    total = df["amount"].sum()

    this_month = df[
        (df["date"].dt.month == date.today().month)
        & (df["date"].dt.year == date.today().year)
    ]["amount"].sum()

    transaction_count = len(df)
    average = total / transaction_count

    # Dashboard summary cards
    
    # Monthly budget
    st.subheader("🎯 Monthly Budget")

    monthly_budget = st.number_input(
        "Set your monthly budget (₹)",
        min_value=1.0,
        value=5000.0,
        step=500.0,
        key="monthly_budget"
    )

    if this_month > monthly_budget:
        st.error("⚠️ You have exceeded your monthly budget!")
    elif this_month >= monthly_budget * 0.8:
        st.warning("You have used 80% or more of your monthly budget.")
    else:
        st.success("You are within your monthly budget.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Spending", f"₹{total:,.2f}")
    col2.metric("This Month", f"₹{this_month:,.2f}")
    col3.metric("Transactions", transaction_count)
    col4.metric("Average Expense", f"₹{average:,.2f}")

    st.divider()

    # Two-column dashboard layout
    left, right = st.columns(2)

    # Donut chart: Spending by category
    with left:
        st.subheader("Spending by Category")

        category_totals = (
            df.groupby("category", as_index=False)["amount"].sum()
        )

        st.vega_lite_chart(
            category_totals,
            {
                "mark": {
                    "type": "arc",
                    "innerRadius": 70
                },
                "encoding": {
                    "theta": {
                        "field": "amount",
                        "type": "quantitative"
                    },
                    "color": {
                        "field": "category",
                        "type": "nominal",
                        "legend": {
                            "title": "Category"
                        }
                    },
                    "tooltip": [
                        {
                            "field": "category",
                            "type": "nominal"
                        },
                        {
                            "field": "amount",
                            "type": "quantitative",
                            "title": "Amount (₹)"
                        }
                    ]
                },
                "height": 300
            },
            use_container_width=True
        )

    # Recent expenses
    with right:
        st.subheader("Recent Expenses")

        recent = df.sort_values(
            "date",
            ascending=False
        )

        st.dataframe(
            recent[
                ["date", "description", "category", "amount"]
            ],
            use_container_width=True,
            hide_index=True
        )

    # Delete an expense
    st.divider()
    st.subheader("Delete an Expense")

    expense_options = []

    for i, expense in enumerate(expenses):
        label = (
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description'] or 'No description'}"
        )

        expense_options.append((label, i))

    selected_expense = st.selectbox(
        "Choose an expense to delete",
        expense_options,
        format_func=lambda item: item[0],
        key="delete_expense_select"
    )

    if st.button("Delete Selected Expense", type="primary"):
        index = selected_expense[1]

        st.session_state.expenses.pop(index)
        save_expenses(st.session_state.expenses)

        st.success("Expense deleted successfully!")
        st.rerun()

    # All transactions
    st.divider()
    
    # Monthly spending chart
    st.divider()
    st.subheader("📅 Monthly Spending Trend")

    monthly_data = df.copy()
    monthly_data["month"] = (
        monthly_data["date"].dt.to_period("M").astype(str)
    )

    monthly_totals = (
        monthly_data.groupby("month")["amount"].sum()
    )

    st.bar_chart(monthly_totals)

    st.subheader("All Transactions")

    st.dataframe(
        df.sort_values("date", ascending=False),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info(
        "No expenses yet. Add your first expense using the sidebar."
    )

