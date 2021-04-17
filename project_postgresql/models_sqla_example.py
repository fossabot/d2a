# Code generated by d2a (https://github.com/walkframe/d2a).
# `./manage.py sqla_codegen --settings=settings.codegen --path=models_sqla_example.py` at Sat Apr 17 04:57:15 2021 UTC.

import os
from importlib import import_module

import sqlalchemy as sa
from sqlalchemy import (
    types as default_types,
    Column,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import (
    postgresql as postgresql_types,
    mysql as mysql_types,
    oracle as oracle_types,
)
from django.utils import timezone
from d2a import original_types
try:
    from geoalchemy2 import types as geotypes
except ImportError:
    pass

# import finished

Base = declarative_base()


def GET_DEFAULT(path):
    '''DO NOT DELETE THIS FUNCTION'''

    module_path, model_name, field_name = path.rsplit(".", 2)
    try:
        module = import_module(module_path)
        model = getattr(module, model_name)
    except (ImportError, AttributeError):
        return None

    for field in model._meta.fields:
        if field.name == field_name:
            return field.default


# start defining models



class ContentType(Base):
    __tablename__ = 'django_content_type'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    app_label = Column(
        postgresql_types.VARCHAR(length=100),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    model = Column(
        postgresql_types.VARCHAR(length=100),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )


class LogEntry(Base):
    __tablename__ = 'django_admin_log'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    action_time = Column(
        postgresql_types.TIMESTAMP(),
        default=GET_DEFAULT('django.contrib.admin.models.LogEntry.action_time'),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    user_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_user.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    content_type_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="django_content_type.id", ondelete="SET_NULL"),
        primary_key=False,
        unique=False,
        nullable=True,
        autoincrement=True,
        doc="testtest",
    )
    object_id = Column(
        postgresql_types.TEXT(),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    object_repr = Column(
        postgresql_types.VARCHAR(length=200),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    action_flag = Column(
        postgresql_types.SMALLINT(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    change_message = Column(
        postgresql_types.TEXT(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    user = relationship(
        'User',
        foreign_keys="[django_admin_log.c.user_id]",
        remote_side=None,
        backref="logentry",
    )
    content_type = relationship(
        'ContentType',
        foreign_keys="[django_admin_log.c.content_type_id]",
        remote_side=None,
        backref="logentry",
    )


class GroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    group_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_group.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    permission_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_permission.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    group = relationship(
        'Group',
        foreign_keys="[auth_group_permissions.c.group_id]",
        remote_side=None,
        backref="group_permissions",
    )
    permission = relationship(
        'Permission',
        foreign_keys="[auth_group_permissions.c.permission_id]",
        remote_side=None,
        backref="group_permissions",
    )


class Group(Base):
    __tablename__ = 'auth_group'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    name = Column(
        postgresql_types.VARCHAR(length=150),
        primary_key=False,
        unique=True,
        nullable=False,
        doc="testtest",
    )
    permissions = relationship(
        'Permission',
        secondary="auth_group_permissions",
        foreign_keys="[auth_group_permissions.c.group_id, auth_group_permissions.c.permission_id]",
        remote_side=None,
        backref="group",
    )


class Permission(Base):
    __tablename__ = 'auth_permission'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    name = Column(
        postgresql_types.VARCHAR(length=255),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    content_type_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="django_content_type.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    codename = Column(
        postgresql_types.VARCHAR(length=100),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    content_type = relationship(
        'ContentType',
        foreign_keys="[auth_permission.c.content_type_id]",
        remote_side=None,
        backref="permission",
    )


class UserGroups(Base):
    __tablename__ = 'auth_user_groups'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    user_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_user.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    group_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_group.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    user = relationship(
        'User',
        foreign_keys="[auth_user_groups.c.user_id]",
        remote_side=None,
        backref="user_groups",
    )
    group = relationship(
        'Group',
        foreign_keys="[auth_user_groups.c.group_id]",
        remote_side=None,
        backref="user_groups",
    )


class UserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    user_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_user.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    permission_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="auth_permission.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    user = relationship(
        'User',
        foreign_keys="[auth_user_user_permissions.c.user_id]",
        remote_side=None,
        backref="user_user_permissions",
    )
    permission = relationship(
        'Permission',
        foreign_keys="[auth_user_user_permissions.c.permission_id]",
        remote_side=None,
        backref="user_user_permissions",
    )


class User(Base):
    __tablename__ = 'auth_user'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    password = Column(
        postgresql_types.VARCHAR(length=128),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    last_login = Column(
        postgresql_types.TIMESTAMP(),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    is_superuser = Column(
        mysql_types.BOOLEAN(),
        default=GET_DEFAULT('django.contrib.auth.models.User.is_superuser'),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    username = Column(
        postgresql_types.VARCHAR(length=150),
        primary_key=False,
        unique=True,
        nullable=False,
        doc="testtest",
    )
    first_name = Column(
        postgresql_types.VARCHAR(length=150),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    last_name = Column(
        postgresql_types.VARCHAR(length=150),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    email = Column(
        postgresql_types.VARCHAR(length=254),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    is_staff = Column(
        mysql_types.BOOLEAN(),
        default=GET_DEFAULT('django.contrib.auth.models.User.is_staff'),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    is_active = Column(
        mysql_types.BOOLEAN(),
        default=GET_DEFAULT('django.contrib.auth.models.User.is_active'),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    date_joined = Column(
        postgresql_types.TIMESTAMP(),
        default=GET_DEFAULT('django.contrib.auth.models.User.date_joined'),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    groups = relationship(
        'Group',
        secondary="auth_user_groups",
        foreign_keys="[auth_user_groups.c.user_id, auth_user_groups.c.group_id]",
        remote_side=None,
        backref="user",
    )
    user_permissions = relationship(
        'Permission',
        secondary="auth_user_user_permissions",
        foreign_keys="[auth_user_user_permissions.c.user_id, auth_user_user_permissions.c.permission_id]",
        remote_side=None,
        backref="user",
    )


class Session(Base):
    __tablename__ = 'django_session'
    
    session_key = Column(
        postgresql_types.VARCHAR(length=40),
        primary_key=True,
        unique=True,
        nullable=False,
        doc="testtest",
    )
    session_data = Column(
        postgresql_types.TEXT(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    expire_date = Column(
        postgresql_types.TIMESTAMP(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )


class Author(Base):
    __tablename__ = 'author'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    name = Column(
        postgresql_types.VARCHAR(length=255),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    age = Column(
        postgresql_types.SMALLINT(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    email = Column(
        postgresql_types.VARCHAR(length=254),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )


class BookCategory(Base):
    __tablename__ = 'book_category'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    book_id = Column(
        postgresql_types.UUID(),
        ForeignKey(column="book.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    category_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="category.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    book = relationship(
        'Book',
        foreign_keys="[book_category.c.book_id]",
        remote_side=None,
        backref="book_category",
    )
    category = relationship(
        'Category',
        foreign_keys="[book_category.c.category_id]",
        remote_side=None,
        backref="book_category",
    )


class Book(Base):
    __tablename__ = 'book'
    
    id = Column(
        postgresql_types.UUID(),
        default=GET_DEFAULT('books.models.Book.id'),
        primary_key=True,
        unique=True,
        nullable=False,
        doc="testtest",
    )
    price = Column(
        postgresql_types.JSONB(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    title = Column(
        default_types.VARCHAR(length=255),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    description = Column(
        postgresql_types.TEXT(),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    author_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="author.id", ondelete="SET_NULL"),
        primary_key=False,
        unique=False,
        nullable=True,
        autoincrement=True,
        doc="testtest",
    )
    content = Column(
        postgresql_types.BYTEA(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    tags = Column(
        postgresql_types.ARRAY(item_type=postgresql_types.VARCHAR, dimensions=1),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    author = relationship(
        'Author',
        foreign_keys="[book.c.author_id]",
        remote_side=None,
        backref="books",
    )
    category = relationship(
        'Category',
        secondary="book_category",
        foreign_keys="[book_category.c.book_id, book_category.c.category_id]",
        remote_side=None,
        backref="books",
        lazy="joined",
    )


class CategoryRelation(Base):
    __tablename__ = 'category_relation'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    category1_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="category.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    category2_id = Column(
        postgresql_types.INTEGER(),
        ForeignKey(column="category.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    type = Column(
        postgresql_types.VARCHAR(length=30),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    category1 = relationship(
        'Category',
        foreign_keys="[category_relation.c.category1_id]",
        remote_side=None,
        backref="parents",
    )
    category2 = relationship(
        'Category',
        foreign_keys="[category_relation.c.category2_id]",
        remote_side=None,
        backref="children",
    )


class Category(Base):
    __tablename__ = 'category'
    
    id = Column(
        postgresql_types.INTEGER(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    name = Column(
        original_types.CIText(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    created = Column(
        postgresql_types.TIMESTAMP(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    related_coming = relationship(
        'Category',
        secondary="category_relation",
        foreign_keys="[category_relation.c.category1_id]",
        remote_side="[category.c.id]",
        backref="related_going",
    )


class Sales(Base):
    __tablename__ = 'sales'
    
    id = Column(
        postgresql_types.BIGINT(),
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
        doc="testtest",
    )
    book_id = Column(
        postgresql_types.UUID(),
        ForeignKey(column="book.id", ondelete="CASCADE"),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    sold = Column(
        postgresql_types.TIMESTAMP(),
        primary_key=False,
        unique=False,
        nullable=False,
        doc="testtest",
    )
    reservation = Column(
        postgresql_types.INTERVAL(),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    source = Column(
        postgresql_types.INET(),
        primary_key=False,
        unique=False,
        nullable=True,
        doc="testtest",
    )
    book = relationship(
        'Book',
        foreign_keys="[sales.c.book_id]",
        remote_side=None,
        backref="sales",
    )


# END OF FILE
