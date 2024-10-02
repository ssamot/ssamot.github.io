alias updl="git add -A -v; git commit -m "fixes"; git push origin"
new_post() {
  echo $1
  hugo new posts/$1.md
  mate content/posts/$1.md
}
