from custommodels import Checkpoint, db, User

def create_checkpoints():
    rules = [(1, 'All pages should contain headings.', '(?s)(?i)<h[\\d][^>]*>'), 
    (2, 'All pages should contain an H1 heading.', '(?s)(?i)<h1\\b[^>]*>'), 
    (3, 'All pages should contain a title tag.', '(?s)(?i)<title\\b[^>]*>[^<>]+?<\\/title>'), 
    (4, 'Do not use inline styles.', '(?s)(?i)<[^>]*style=["\'](?!\\s*?display\\s*?:\\s*?none|\\s*?visibility\\s*?:\\s*?hidden|\\s*["\'])[^"\']*["\'][^>]*>')]

    for r in rules:
        wcaglevels = 'A, AA'
        benefits = 'Accessibility, SEO'
        Checkpoint(r[1], wcaglevels, benefits, r[2], None)
    return

def create_admin():
    User('Joao', 'admin@admin.com', 'joao')
    return

if __name__ == "__main__":
    try:
        db.drop_all()
        db.create_all()
        create_checkpoints()
        create_admin()
        print('Database restarted and populated!')
    except BaseException as e:
        print(f'Something went wrong here. [The error] -> {e}')