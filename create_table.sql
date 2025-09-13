CREATE TABLE
    PRODUCTS
        (
            PRODUCT_CODE VARCHAR(8) PRIMARY KEY,
            PRODUCT_NAME VARCHAR(100)
        );

CREATE TABLE
    PRODUCT_VARIANTS
        (
            PRODUCT_CODE VARCHAR(8),
            VARIANT_CODE VARCHAR(2),
            COLOR_CODE VARCHAR(2),
            PRICE INT(10),
            RELEASE_DATE VARCHAR(8),
            PRIMARY KEY(PRODUCT_CODE,VARIANT_CODE)
        );

CREATE TABLE
    PRODUCT_IMAGE
        (
            PRODUCT_CODE VARCHAR(8),
            VARIANT_CODE VARCHAR(2),
            PRIORITY_NUMBER INT(2),
            THUMBNAIL_FLAG VARCHAR(1),
            IMAGE_URL TEXT,
            PRIMARY KEY(PRODUCT_CODE,VARIANT_CODE,PRIORITY_NUMBER)
        );

CREATE TABLE
    PURCHASE_HISTORY
        (
            PURCHASE_NUMBER INT(10) PRIMARY KEY,
            PURCHASE_DATETIME VARCHAR(14),
            PRODUCT_CODE VARCHAR(8),
            VARIANT_CODE VARCHAR(2),
            QUANTITY INT(2)
        );
