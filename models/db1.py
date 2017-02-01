Post = db.define_table("post",
	Field("message", "text", requires=IS_NOT_EMPTY(), notnull=True),
	auth.signature
	)
Post.is_active.readable = False
Post.is_active.writable = False