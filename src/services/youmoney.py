from yoomoney import Authorize

Authorize(
      client_id="10CF0FC11627302FB64709A07B98E2E1A149633980729F8A518F00FAE8A21A10",
      redirect_uri="https://t.me/Sherlok78Bot",
      scope=["account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop",
             ]
      )

