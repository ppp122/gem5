#include "jiajia_object.hh"
#include <iostream>

namespace gem5
{

JiajiaObject::JiajiaObject(const JiajiaObjectParams &params) :
    SimObject(params)
{
    std::cout << "Hello World! jiajia From a SimObject!" << std::endl;
}

} // namespace gem5
