import pandas as pd
import logging

class DeliveryPerformanceReportGenerator:
    def generate_delivery_performance_report(self, orders_data, delivery_data):
        df_orders = pd.DataFrame(orders_data)
        df_delivery = pd.DataFrame(delivery_data)

        merged_df = pd.merge(df_orders, df_delivery, on="order_id")

        # Placeholder for delivery performance analysis (replace it with your actual analysis logic)
        delivery_performance_analysis = merged_df.groupby("delivery_person")["delivery_time"].mean().reset_index()

        report_path = "delivery_performance_report.csv"
        delivery_performance_analysis.to_csv(report_path, index=False)
        logging.info(f"Delivery Performance Report generated and saved at: {report_path}")
        return report_path
