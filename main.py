from config import MONGO_URI
from mongodb_connector import MongoDBConnector
from feedback_report_generator import FeedbackReportGenerator
from combined_report_generator import CombinedReportGenerator
from delivery_performance_report_generator import DeliveryPerformanceReportGenerator
from user_order_history_report_generator import UserOrderHistoryReportGenerator
from email_sender import EmailSender
from aws_s3_uploader import S3Uploader
import logging

def main():
    logging.basicConfig(filename='food_delivery.log', level=logging.INFO)

    try:
        # Connect to MongoDB
        mongo_connector = MongoDBConnector(MONGO_URI)

        # Fetch data from MongoDB for different reports
        users_data = mongo_connector.get_data("users")
        orders_data = mongo_connector.get_data("orders")
        products_data = mongo_connector.get_data("products")
        feedback_data = mongo_connector.get_data("feedback")
        delivery_data = mongo_connector.get_data("delivery")

        # Generate reports
        feedback_report_generator = FeedbackReportGenerator()
        combined_report_generator = CombinedReportGenerator()
        delivery_performance_report_generator = DeliveryPerformanceReportGenerator()
        user_order_history_report_generator = UserOrderHistoryReportGenerator()

        feedback_report_path = feedback_report_generator.generate_feedback_report(users_data, feedback_data)
        combined_report_path = combined_report_generator.generate_combined_report(orders_data, products_data, users_data)
        delivery_performance_report_path = delivery_performance_report_generator.generate_delivery_performance_report(orders_data, delivery_data)
        user_order_history_report_path = user_order_history_report_generator.generate_user_order_history_report(users_data, orders_data, products_data)

        # Send reports via email
        email_sender = EmailSender()
        email_sender.send_email("Feedback Report", "Please find attached the feedback report.", feedback_report_path)
        email_sender.send_email("Combined Report", "Please find attached the combined report.", combined_report_path)
        email_sender.send_email("Delivery Performance Report", "Please find attached the delivery performance report.", delivery_performance_report_path)
        email_sender.send_email("User Order History Report", "Please find attached the user order history report.", user_order_history_report_path)

        # Upload reports to AWS S3
        s3_uploader = S3Uploader()
        s3_uploader.upload_to_s3(feedback_report_path, "feedback_report.csv")
        s3_uploader.upload_to_s3(combined_report_path, "combined_report.csv")
        s3_uploader.upload_to_s3(delivery_performance_report_path, "delivery_performance_report.csv")
        s3_uploader.upload_to_s3(user_order_history_report_path, "user_order_history_report.csv")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
