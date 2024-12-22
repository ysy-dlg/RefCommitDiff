#!/usr/bin/env ruby

FNAME_RE = /^([^\#]+)\#([^\(]+)\(([^\)]+)\)\.mjava$/i

def parse_fname(fname)
  if FNAME_RE =~ fname
    [ $1, $2, $3 ]
  else
    nil
  end
end

def process_rename(old_fname, new_fname)
  o = parse_fname(old_fname)
  n = parse_fname(new_fname)
  return nil unless o && n

  if o[0] == n[0]
    if o[2] == n[2]
      "Rename Method: '#{o[1]}' to '#{n[1]}' at '#{o[0]}'"
    elsif o[1] == o[1]
      "Change Parameter: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    else
      "Rename Method+: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    end
  elsif o[1] == n[1]
    if o[2] == n[2]
      "Move Method: '#{o[1]}' from '#{o[0]}' to '#{n[0]}'"
    else
      "Move Method+: '#{o[1]}(#{o[2]})' to '#{n[1]}(#{n[2]})' at '#{o[0]}'"
    end
  elsif o[2] == n[2]
    "Move and Rename Method: '#{o[1]}' at '#{o[0]}' to '#{n[1]}' at '#{n[0]}'"
  else
    "Move and Rename Method+: '#{o[1]}(#{o[2]})' at '#{o[0]}' to '#{n[1]}(#{n[2]})' at '#{n[0]}'"
  end
end

open("| git --git-dir='#{ARGV[0]}' log --branches --tags --no-merges -M50 --name-status --pretty=tformat:'n:%N%h %s'") do |fin|
  fin.each_line do |line|
    line.chomp!
    case line
    when /^n:(.*)/
      $note = $1
    when /^([a-f0-9]+) (.*)/
      $cid, $log = $1, $2
    when /^R(\d+)\t(.*?)\t(.*?)$/
      score, old_fname, new_fname = $1.to_i, $2, $3
      type = process_rename(old_fname, new_fname)
      puts "#{$note[0,10]}\t#{$cid[0,10]}\t#{score}\t#{type}\t#{old_fname}\t#{new_fname}" if type
    end
  end
end

__END__
