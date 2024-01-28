import pandas as pd
import logging

class PaymentTrendsReportGenerator:
    def generate_payment_trends_report(self, orders_data, payments_data):
        df_orders = pd.DataFrame(orders_data)
        df_payments = pd.DataFrame(payments_data)

        merged_df = pd.merge(df_orders, df_payments, on="order_id")

        # Different analysis: Calculate the distribution of payment amounts for each payment method
        payment_trends_analysis = merged_df.groupby("payment_method")["total_amount"].describe().reset_index()

        report_path = "payment_trends_report.csv"
        payment_trends_analysis.to_csv(report_path, index=False)
        logging.info(f"Payment Trends Report generated and saved at: {report_path}")
        return report_path
