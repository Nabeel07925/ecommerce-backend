from repositories.order import OrderRepository
from common import schema
from sqlalchemy.orm import Session


class RevenueComponent:
    @staticmethod
    def get_revenue_in_time_duration(start_date, end_date, product_id, category_id, db):
        orders = OrderRepository.get_orders_in_dates(db=db,
                                                     start_date=start_date,
                                                     end_date=end_date,
                                                     product_filter=product_id,
                                                     category_filter=category_id)

        revenue_res = schema.Revenue(
            start_date= start_date,
            end_date=end_date,
            total_profit=0,
            total_sales=0
        )
        total_sales = 0
        total_cost = 0

        for order in orders:
            for item in order.order_items:
                total_sales += item.inventory.retail_price
                total_cost += item.inventory.invoice_price

        revenue_res.total_sales = total_sales
        revenue_res.total_profit = total_sales - total_cost

        return revenue_res
