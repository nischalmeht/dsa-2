const orders = [
    {
        orderId: 101,
        customer: {
            name: "Alice"
        },
        items: [
            {
                productId: "P001",
                productName: "Laptop",
                reviews: [{ reviewer: "John", rating: 5 }, { reviewer: "Emily", rating: 4 }]
            },
            {
                productId: "P002",
                productName: "Mouse",
                reviews: [{ reviewer: "Mark", rating: 4 }, { reviewer: "Anna", rating: 3 }]
            }
        ]
    },
    {
        orderId: 102,
        customer: {
            name: "Bob"
        },
        items: [
            {
                productId: "P003",
                productName: "Smartphone",
                reviews: [{ reviewer: "Sara", rating: 5 }, { reviewer: "David", rating: 4 }]
            },
            {
                productId: "P004",
                productName: "Headphones",
                reviews: [{ reviewer: "Alice", rating: 5 }, { reviewer: "Tom", rating: 4 }]
            }
        ]
    }
];

const transformedData = orders.flatMap(order =>
    order.items.flatMap(item =>
        item.reviews.map(review => ({
            orderId: order.orderId,
            customerName: order.customer.name,
            productId: item.productId,
            productName: item.productName,
            reviewer: review.reviewer,
            rating: review.rating
        }))
    )
);
console.log('transformedData',transformedData)