import pandas as pd
import logging

class UserOrderHistoryReportGenerator:
    def generate_user_order_history_report(self, users_data, orders_data, products_data):
        df_users = pd.DataFrame(users_data)
        df_orders = pd.DataFrame(orders_data)
        df_products = pd.DataFrame(products_data)

        merged_df = pd.merge(df_orders, df_users, on="user_id")
        merged_df = pd.merge(merged_df, df_products, on="product_id")

        # Placeholder for user order history analysis (replace it with your actual analysis logic)
        user_order_history_analysis = merged_df.groupby(["user_id", "username", "product_name"]).agg({"quantity": "sum"}).reset_index()

        report_path = "user_order_history_report.csv"
        user_order_history_analysis.to_csv(report_path, index=False)
        logging.info(f"User Order History Report generated and saved at: {report_path}")
        return report_path
