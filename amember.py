from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

class AmemberAccessLog(DeclarativeBase):
    __tablename__ = 'amember_access_log'

    #column definitions
    log_id = Column(u'log_id', INTEGER(), primary_key=True, nullable=False)
    member_id = Column(u'member_id', INTEGER(), nullable=False)
    referrer = Column(u'referrer', VARCHAR(length=255))
    remote_addr = Column(u'remote_addr', VARCHAR(length=15))
    time = Column(u'time', TIMESTAMP(), nullable=False)
    url = Column(u'url', VARCHAR(length=255))

    #relation definitions


class AmemberAdmin(DeclarativeBase):
    __tablename__ = 'amember_admins'

    #column definitions
    admin_id = Column(u'admin_id', INTEGER(), primary_key=True, nullable=False)
    email = Column(u'email', VARCHAR(length=255))
    last_ip = Column(u'last_ip', VARCHAR(length=32))
    last_login = Column(u'last_login', DATETIME())
    last_session = Column(u'last_session', VARCHAR(length=32))
    login = Column(u'login', VARCHAR(length=32), nullable=False)
    passwd = Column(u'pass', VARCHAR(length=128), nullable=False) # 'pass' is a reserved word in Python
    perms = Column(u'perms', TEXT())
    super_user = Column(u'super_user', SMALLINT(), nullable=False)

    #relation definitions


class AmemberAdminLog(DeclarativeBase):
    __tablename__ = 'amember_admin_log'

    #column definitions
    admin_id = Column(u'admin_id', INTEGER())
    admin_login = Column(u'admin_login', VARCHAR(length=32))
    dattm = Column(u'dattm', DATETIME())
    ip = Column(u'ip', VARCHAR(length=32))
    log_id = Column(u'log_id', INTEGER(), primary_key=True, nullable=False)
    message = Column(u'message', TEXT())
    record_id = Column(u'record_id', INTEGER(), nullable=False)
    tablename = Column(u'tablename', VARCHAR(length=32), nullable=False)

    #relation definitions


class AmemberAffClick(DeclarativeBase):
    __tablename__ = 'amember_aff_clicks'

    #column definitions
    aff_id = Column(u'aff_id', INTEGER(), nullable=False)
    log_id = Column(u'log_id', INTEGER(), primary_key=True, nullable=False)
    referrer = Column(u'referrer', VARCHAR(length=255))
    remote_addr = Column(u'remote_addr', VARCHAR(length=15))
    time = Column(u'time', TIMESTAMP(), nullable=False)
    url = Column(u'url', VARCHAR(length=255))

    #relation definitions


class AmemberAffCommission(DeclarativeBase):
    __tablename__ = 'amember_aff_commission'

    #column definitions
    aff_id = Column(u'aff_id', INTEGER(), nullable=False)
    amount = Column(u'amount', DECIMAL(precision=12, scale=2))
    commission_id = Column(u'commission_id', INTEGER(), primary_key=True, nullable=False)
    date = Column(u'date', DATE(), nullable=False)
    is_first = Column(u'is_first', INTEGER(), nullable=False)
    payment_id = Column(u'payment_id', INTEGER(), nullable=False)
    payout_id = Column(u'payout_id', CHAR(length=32))
    product_id = Column(u'product_id', INTEGER(), nullable=False)
    receipt_id = Column(u'receipt_id', CHAR(length=32), nullable=False)
    record_type = Column(u'record_type', CHAR(length=16), nullable=False)
    tier = Column(u'tier', SMALLINT())

    #relation definitions


class AmemberConfig(DeclarativeBase):
    __tablename__ = 'amember_config'

    #column definitions
    blob_value = Column(u'blob_value', BLOB())
    config_id = Column(u'config_id', INTEGER(), primary_key=True, nullable=False)
    name = Column(u'name', VARCHAR(length=64), nullable=False)
    type = Column(u'type', SMALLINT())
    value = Column(u'value', VARCHAR(length=255))

    #relation definitions


class AmemberCountry(DeclarativeBase):
    __tablename__ = 'amember_countries'

    #column definitions
    country = Column(u'country', CHAR(length=2), nullable=False)
    country_id = Column(u'country_id', INTEGER(), primary_key=True, nullable=False)
    status = Column(u'status', Enum(u'added', u'changed'))
    tag = Column(u'tag', INTEGER())
    title = Column(u'title', VARCHAR(length=64))

    #relation definitions


class AmemberCoupon(DeclarativeBase):
    __tablename__ = 'amember_coupon'

    #column definitions
    batch_id = Column(u'batch_id', INTEGER(), nullable=False)
    begin_date = Column(u'begin_date', DATE())
    code = Column(u'code', VARCHAR(length=32), nullable=False)
    comment = Column(u'comment', VARCHAR(length=64))
    coupon_id = Column(u'coupon_id', INTEGER(), primary_key=True, nullable=False)
    data = Column(u'data', TEXT())
    discount = Column(u'discount', VARCHAR(length=32), nullable=False)
    expire_date = Column(u'expire_date', DATE())
    is_recurring = Column(u'is_recurring', SMALLINT(), nullable=False)
    locked = Column(u'locked', Integer(), nullable=False)
    member_id = Column(u'member_id', INTEGER(), nullable=False)
    member_use_count = Column(u'member_use_count', INTEGER(), nullable=False)
    product_id = Column(u'product_id', VARCHAR(length=255))
    use_count = Column(u'use_count', INTEGER(), nullable=False)
    used_count = Column(u'used_count', INTEGER(), nullable=False)
    used_for = Column(u'used_for', TEXT())

    #relation definitions


class AmemberCronRun(DeclarativeBase):
    __tablename__ = 'amember_cron_run'

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    time = Column(u'time', DATETIME(), nullable=False)

    #relation definitions


class AmemberEmailTemplate(DeclarativeBase):
    __tablename__ = 'amember_email_templates'

    #column definitions
    attachments = Column(u'attachments', String())
    day = Column(u'day', INTEGER())
    email_template_id = Column(u'email_template_id', INTEGER(), primary_key=True, nullable=False)
    format = Column(u'format', Enum(u'text', u'html', u'multipart'), nullable=False)
    lang = Column(u'lang', VARCHAR(length=16), nullable=False)
    name = Column(u'name', VARCHAR(length=32), nullable=False)
    plain_txt = Column(u'plain_txt', String())
    product_id = Column(u'product_id', INTEGER())
    subject = Column(u'subject', VARCHAR(length=255), nullable=False)
    txt = Column(u'txt', String(), nullable=False)

    #relation definitions


class AmemberErrorLog(DeclarativeBase):
    __tablename__ = 'amember_error_log'

    #column definitions
    error = Column(u'error', TEXT())
    log_id = Column(u'log_id', INTEGER(), primary_key=True, nullable=False)
    member_id = Column(u'member_id', INTEGER())
    referrer = Column(u'referrer', VARCHAR(length=255))
    remote_addr = Column(u'remote_addr', VARCHAR(length=15))
    time = Column(u'time', TIMESTAMP(), nullable=False)
    url = Column(u'url', VARCHAR(length=255))

    #relation definitions


class AmemberFailedLogin(DeclarativeBase):
    __tablename__ = 'amember_failed_login'

    #column definitions
    failed_login_id = Column(u'failed_login_id', INTEGER(), primary_key=True, nullable=False)
    failed_logins = Column(u'failed_logins', INTEGER(), nullable=False)
    ip = Column(u'ip', CHAR(length=15), nullable=False)
    last_failed = Column(u'last_failed', INTEGER(), nullable=False)
    login_type = Column(u'login_type', INTEGER(), nullable=False)

    #relation definitions


class AmemberFolder(DeclarativeBase):
    __tablename__ = 'amember_folders'

    #column definitions
    files_content = Column(u'files_content', BLOB())
    folder_id = Column(u'folder_id', INTEGER(), primary_key=True, nullable=False)
    method = Column(u'method', VARCHAR(length=64))
    path = Column(u'path', VARCHAR(length=255), nullable=False)
    product_ids = Column(u'product_ids', TEXT(), nullable=False)
    url = Column(u'url', VARCHAR(length=255), nullable=False)

    #relation definitions


class AmemberMember(DeclarativeBase):
    __tablename__ = 'amember_members'

    #column definitions
    added = Column(u'added', DATETIME(), nullable=False)
    aff_id = Column(u'aff_id', INTEGER())
    aff_payout_type = Column(u'aff_payout_type', VARCHAR(length=32))
    city = Column(u'city', VARCHAR(length=255))
    country = Column(u'country', VARCHAR(length=255))
    data = Column(u'data', TEXT(), nullable=False)
    email = Column(u'email', VARCHAR(length=64))
    email_verified = Column(u'email_verified', Integer())
    is_affiliate = Column(u'is_affiliate', Integer())
    is_male = Column(u'is_male', SMALLINT())
    login = Column(u'login', VARCHAR(length=32), nullable=False)
    member_id = Column(u'member_id', INTEGER(), primary_key=True, nullable=False)
    name_f = Column(u'name_f', VARCHAR(length=32), nullable=False)
    name_l = Column(u'name_l', VARCHAR(length=32), nullable=False)
    passwd = Column(u'pass', VARCHAR(length=32)) # 'pass' is a reserved word in Python
    remote_addr = Column(u'remote_addr', VARCHAR(length=15))
    security_code = Column(u'security_code', VARCHAR(length=40))
    securitycode_expire = Column(u'securitycode_expire', DATETIME())
    state = Column(u'state', VARCHAR(length=255))
    status = Column(u'status', SMALLINT(), nullable=False)
    street = Column(u'street', VARCHAR(length=255))
    unsubscribed = Column(u'unsubscribed', Integer())
    zip = Column(u'zip', VARCHAR(length=255))

    #relation definitions


class AmemberNewsletterArchive(DeclarativeBase):
    __tablename__ = 'amember_newsletter_archive'

    #column definitions
    add_date = Column(u'add_date', DATETIME())
    archive_id = Column(u'archive_id', INTEGER(), primary_key=True, nullable=False)
    is_html = Column(u'is_html', SMALLINT(), nullable=False)
    message = Column(u'message', TEXT())
    subject = Column(u'subject', VARCHAR(length=255), nullable=False)
    threads = Column(u'threads', VARCHAR(length=255), nullable=False)

    #relation definitions


class AmemberNewsletterGuest(DeclarativeBase):
    __tablename__ = 'amember_newsletter_guest'

    #column definitions
    guest_email = Column(u'guest_email', VARCHAR(length=60), nullable=False)
    guest_id = Column(u'guest_id', INTEGER(), primary_key=True, nullable=False)
    guest_name = Column(u'guest_name', VARCHAR(length=60), nullable=False)
    security_code = Column(u'security_code', VARCHAR(length=40))
    securitycode_expire = Column(u'securitycode_expire', DATETIME())

    #relation definitions


class AmemberNewsletterGuestSubscription(DeclarativeBase):
    __tablename__ = 'amember_newsletter_guest_subscriptions'

    #column definitions
    guest_id = Column(u'guest_id', INTEGER(), nullable=False)
    guest_subscription_id = Column(u'guest_subscription_id', INTEGER(), primary_key=True, nullable=False)
    security_code = Column(u'security_code', VARCHAR(length=40))
    securitycode_expire = Column(u'securitycode_expire', DATETIME())
    thread_id = Column(u'thread_id', INTEGER(), nullable=False)

    #relation definitions


class AmemberNewsletterMemberSubscription(DeclarativeBase):
    __tablename__ = 'amember_newsletter_member_subscriptions'

    #column definitions
    member_id = Column(u'member_id', INTEGER(), nullable=False)
    member_subscription_id = Column(u'member_subscription_id', INTEGER(), primary_key=True, nullable=False)
    status = Column(u'status', SMALLINT(), nullable=False)
    thread_id = Column(u'thread_id', INTEGER(), nullable=False)

    #relation definitions


class AmemberNewsletterThread(DeclarativeBase):
    __tablename__ = 'amember_newsletter_thread'

    #column definitions
    blob_auto_subscribe = Column(u'blob_auto_subscribe', BLOB())
    blob_available_to = Column(u'blob_available_to', BLOB())
    description = Column(u'description', TEXT())
    is_active = Column(u'is_active', SMALLINT(), nullable=False)
    thread_id = Column(u'thread_id', INTEGER(), primary_key=True, nullable=False)
    title = Column(u'title', VARCHAR(length=60), nullable=False)

    #relation definitions


class AmemberPayment(DeclarativeBase):
    __tablename__ = 'amember_payments'

    #column definitions
    aff_id = Column(u'aff_id', INTEGER(), nullable=False)
    amount = Column(u'amount', DECIMAL(precision=12, scale=2), nullable=False)
    begin_date = Column(u'begin_date', DATE(), nullable=False)
    completed = Column(u'completed', SMALLINT())
    coupon_id = Column(u'coupon_id', INTEGER(), nullable=False)
    data = Column(u'data', TEXT())
    expire_date = Column(u'expire_date', DATE(), nullable=False)
    member_id = Column(u'member_id', INTEGER(), ForeignKey('amember_members.member_id'), nullable=False)
    payer_id = Column(u'payer_id', VARCHAR(length=255), nullable=False)
    payment_id = Column(u'payment_id', INTEGER(), primary_key=True, nullable=False)
    paysys_id = Column(u'paysys_id', VARCHAR(length=32), nullable=False)
    product_id = Column(u'product_id', INTEGER(), ForeignKey('amember_products.product_id'), nullable=False)
    receipt_id = Column(u'receipt_id', VARCHAR(length=32), nullable=False)
    remote_addr = Column(u'remote_addr', VARCHAR(length=15), nullable=False)
    tax_amount = Column(u'tax_amount', DECIMAL(precision=12, scale=2), nullable=False)
    time = Column(u'time', TIMESTAMP(), nullable=False)
    tm_added = Column(u'tm_added', DATETIME(), nullable=False)
    tm_completed = Column(u'tm_completed', DATETIME())

    #relation definitions
    member = relationship("AmemberMember", backref=backref('payments'))
    product = relationship("AmemberProduct", backref=backref('payment'))


class AmemberProduct(DeclarativeBase):
    __tablename__ = 'amember_products'

    #column definitions
    data = Column(u'data', TEXT())
    description = Column(u'description', TEXT())
    price = Column(u'price', DECIMAL(precision=12, scale=2))
    product_id = Column(u'product_id', INTEGER(), primary_key=True, nullable=False)
    title = Column(u'title', VARCHAR(length=255), nullable=False)

    #relation definitions


class AmemberProductsLink(DeclarativeBase):
    __tablename__ = 'amember_products_links'

    #column definitions
    link_comment = Column(u'link_comment', TEXT(), nullable=False)
    link_duration = Column(u'link_duration', VARCHAR(length=10), nullable=False)
    link_files_path = Column(u'link_files_path', TEXT(), nullable=False)
    link_group_id = Column(u'link_group_id', INTEGER())
    link_id = Column(u'link_id', INTEGER(), primary_key=True, nullable=False)
    link_path = Column(u'link_path', VARCHAR(length=255))
    link_product_id = Column(u'link_product_id', INTEGER(), nullable=False)
    link_protected = Column(u'link_protected', SMALLINT())
    link_start_delay = Column(u'link_start_delay', VARCHAR(length=10), nullable=False)
    link_title = Column(u'link_title', VARCHAR(length=255))
    link_url = Column(u'link_url', VARCHAR(length=255))
    time = Column(u'time', TIMESTAMP(), nullable=False)

    #relation definitions


class AmemberProductsLinksGroup(DeclarativeBase):
    __tablename__ = 'amember_products_links_groups'

    #column definitions
    description = Column(u'description', VARCHAR(length=255))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    priority = Column(u'priority', INTEGER())
    title = Column(u'title', VARCHAR(length=255), nullable=False)

    #relation definitions


class AmemberRebillLog(DeclarativeBase):
    __tablename__ = 'amember_rebill_log'

    #column definitions
    added_tm = Column(u'added_tm', DATETIME(), nullable=False)
    amount = Column(u'amount', DECIMAL(precision=12, scale=2), nullable=False)
    payment_date = Column(u'payment_date', DATE(), nullable=False)
    payment_id = Column(u'payment_id', INTEGER(), nullable=False)
    rebill_log_id = Column(u'rebill_log_id', INTEGER(), primary_key=True, nullable=False)
    rebill_payment_id = Column(u'rebill_payment_id', INTEGER(), nullable=False)
    status = Column(u'status', SMALLINT())
    status_msg = Column(u'status_msg', VARCHAR(length=255))
    status_tm = Column(u'status_tm', DATETIME())

    #relation definitions


class AmemberState(DeclarativeBase):
    __tablename__ = 'amember_states'

    #column definitions
    country = Column(u'country', CHAR(length=2), nullable=False)
    state = Column(u'state', CHAR(length=12), nullable=False)
    state_id = Column(u'state_id', INTEGER(), primary_key=True, nullable=False)
    status = Column(u'status', Enum(u'added', u'changed'))
    tag = Column(u'tag', INTEGER())
    title = Column(u'title', VARCHAR(length=64))

    #relation definitions

