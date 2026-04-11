description = [[
Retrieves basic HTTP server information including:
- Server header
- HTTP status code
- Page title
]]

author = "Your Name"
license = "Same as Nmap"
categories = {"discovery", "safe"}

portrule = function(host, port)
    return port.protocol == "tcp" and (port.number == 80 or port.number == 8080)
end

action = function(host, port)
    local http = require "http"
    local shortport = require "shortport"

    local response = http.get(host, port, "/")

    if not response then
        return "No response from server"
    end

    local result = ""

    -- HTTP Status Code
    if response.status then
        result = result .. "Status Code: " .. response.status .. "\n"
    end

    -- Server Header
    if response.header and response.header["server"] then
        result = result .. "Server: " .. response.header["server"] .. "\n"
    end

    -- Extract Page Title
    if response.body then
        local title = string.match(response.body, "<title>(.-)</title>")
        if title then
            result = result .. "Page Title: " .. title .. "\n"
        else
            result = result .. "Page Title: Not found\n"
        end
    end

    return result
end
